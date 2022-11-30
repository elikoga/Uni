# 2022-11-23

A1:

```riscv
# Aufgabe1.s
#
        .data                   # start data section
answer: .string "Result = "
argument: .word   5

        .text                   # start text section
main:   lw  a0, argument        # Load argument from static data
        addi t0, a0, 0          # load 5 into t0
        addi t1, zero, 1
        and  t2, t2, zero

loop:   beqz  t0,  done
        add  t2, t2, t1
        addi  t0, t0, -1
        slli  t1, t1, 1
        j    loop

done:   la a0, answer           # load address of string into a0
        li a7, 4                # code for printing string
        ecall
        mv a0, t2               # move result to a0
        li a7, 36               # code for printing an unsigned integer
        ecall
        li a7, 10               # load environment call code for exit
        ecall
```

b)

Assembly macht folgendes:

Es rechnet 2^argument-1 aus und gibt das Ergebnis zurück.

Es macht es indem es soviele Bits wie argument in t2 auf 1 setzt, vom LSB aus.

c)

Was sind Pseudo-Instruktionen?

Psuedo-Instruktionen sind Instruktionen, die nicht direkt in Maschinensprache übersetzt werden können, sondern in eine Sequenz von Instruktionen übersetzt werden.

Der Assembler übersetzt sie in eine Sequenz von Instruktionen, die das gleiche Ergebnis haben.

Welche Pseudo-Instruktionen müssen im Beispielprogramm umgewandelt werden?

`beqz t0, done` wird in `beq t0, x0, done` übersetzt.

`j loop` wird in `jal x0, loop` übersetzt.

`li a7, 4` kann in eine Reihe von verschiedenen Instruktionen übersetzt werden.
In der Referenz ist das mit "Myriad sequences" beschrieben.
Eine Umsetzung könnte sein: `addi a7, x0, 4`.

`mv a0, t2` wird in `addi a0, t2, 0` übersetzt.

`li a7, 36` wird in `addi a7, x0, 36` übersetzt, wie oben.

`li a7, 10` wird in `addi a7, x0, 10` übersetzt, wie oben.

d) Erweiterung des Programms

Negativcheck + Fehlermeldung

```riscv
# Aufgabe1.s
#

.data
        answer: .string "Result = "
        argument: .word   5
        errormessage: .string "Error: Argument must be positive: "

.text
main:   lw  a0, argument # load word: a0 <- argument
        addi t0, a0, 0 # add immediate: t0 <- a0 + 0
        addi t1, zero, 1 # add immediate: t1 <- 0 + 1
        and  t2, t2, zero # and: t2 <- t2 & 0 # clear t2

        bltz t0, error # branch if less than zero: if t0 < 0 then goto error
        # translated to: blt t0, x0, error

loop:   beqz  t0,  done # branch if equal to zero: if t0 == 0 then goto done
        add  t2, t2, t1 # add: t2 <- t2 + t1
        addi  t0, t0, -1 # add immediate: t0 <- t0 + -1
        slli  t1, t1, 1 # shift left logical immediate: t1 <- t1 << 1
        j    loop # jump: goto loop

error:  la a0, errormessage # load address: a0 <- errormessage
        li a7, 4 # load immediate: a7 <- 4
        ecall # environment call: print string
        li a7, 10 # load immediate: a7 <- 10
        ecall # environment call: exit

done:   la a0, answer # load address: a0 <- answer
        li a7, 4 # load immediate: a7 <- 4
        ecall # environment call: print string
        mv a0, t2 # move: a0 <- t2
        li a7, 36 # load immediate: a7 <- 36
        ecall # environment call: print unsigned integer
        li a7, 10 # load immediate: a7 <- 10
        ecall # environment call: exit
```

---

Aufgabe 2:

```text
Um Daten im Speicher abzulegen gibt es verschieden RISC-V-Direktive, wie z.B. .data,
.byte, .word, .string, usw.. In dieser Aufgabe sollen verschiedenen Daten im Spei-
cher abgelegt werden und ausgegeben werden.
(1) Legen Sie zun ̈achst den Satz ”Hello World!\n“ im Datenabschnitt des Speichers
(beginnend ab der Speicheradresse 0x10000000) ab. Nutzen Sie einen geeigneten
”ecall“ um den gespeicherten Satz auszugeben.
(2) Legen Sie nun zus ̈atzlich die Werte 1 − 10 in je einem Byte des Speichers ab, begin-
nend mit der ersten Wortadresse nach ”Hello World!\n\0“. Geben Sie die Zahlen
ebenfalls aus.
(3) Lege das Datenwort .word 0xdeadbeef im Speicher ab. Werden die Daten mit Hilfe
der Little Endian oder der Big Endian Methode im Speicher abgelegt? Erl ̈autern
Sie.
```

(1)
```riscv
.data
        hello: .string "Hello World!\n"

.text
main:   la a0, hello # load address: a0 <- hello
        li a7, 4 # load immediate: a7 <- 4
        ecall # environment call: print string
        li a7, 10 # load immediate: a7 <- 10
        ecall # environment call: exit
```

(2)
```riscv
.data
        hello: .string "Hello World!\n"
        newline: .string "\n"
        mask: .4byte 0x000000ff
        one: .byte 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

.text
main:   la a0, hello # load address: a0 <- hello
        li a7, 4 # load immediate: a7 <- 4
        ecall # environment call: print string

        # t3 = 10, t2 = one
        addi t3, x0, 10 # add immediate: t3 <- 0 + 10
        la t2, one # load address: t2 <- one

loop:   beqz  t3,  done # branch if equal to zero: if t3 == 0 then goto done


        addi a0, t2, 0 # add immediate: a0 <- t2 + 0
        lb a0, 0(a0) # load byte: a0 <- a0
        # apply mask to get only the last byte
        # lw t0, mask # load word: t0 <- mask
        # and a0, a0, t0 # and: a0 <- a0 & t0
        li a7, 36 # load immediate: a7 <- 36
        ecall # environment call: print unsigned integer

        la a0, newline # load address: a0 <- newline
        li a7, 4 # load immediate: a7 <- 4
        ecall # environment call: print string

        addi t3, t3, -1 # add immediate: t3 <- t3 + -1
        addi t2, t2, 1 # add immediate: t2 <- t2 + 1
        j    loop # jump: goto loop

done:   li a7, 10 # load immediate: a7 <- 10
        ecall # environment call: exit
```

(3)

```riscv
.data
  deadbeef: .word 0xdeadbeef
```

Siehe ![Screenshot 2022-11-23 172131.png](./Screenshot%202022-11-23%20172131.png)

Man sieht: die LSB sind zuerst im Speicher abgelegt. Das ist die Little Endian Methode.

---

Aufgabe 3:

```text
Aufgabe 3 (Stringverarbeitung)
Im folgenden Programm sollen Sie einen im Speicher abgelegten String bearbeiten. Der
String besteht ausschließlich aus Großbuchstaben, die im ASCII-Format kodiert sind.
Ein ASCII-Zeichen wird dabei genau durch ein Byte kodiert. Ihre Aufgabe ist nun, die
einzelnen Großbuchstaben in Kleinbuchstaben umzuwandeln, den ver ̈anderten String im
Speicher abzulegen und ihn erneut auf der Konsole auszugeben. Da die Großbuchstaben
sich in der ASCII-Tabelle an den Positionen 65-90 befinden und die Kleinbuchstaben an
den Positionen 97-122, ist es ausreichend, einen Offset von 32 zu einem Großbuchstaben
zu addieren, um ihn zu einem Kleinbuchstaben zu machen. Verwenden Sie das folgende
Codeger ̈ust, welches einen String byteweise, d.h. Zeichen f ̈ur Zeichen, auf der Konsole
ausgibt. F ̈ur die Ausgabe werden dabei environment calls genutzt. Diese erwarten im
Register a7 einen Code f ̈ur eine Aktion, die auf Register a0 ausgef ̈uhrt wird. In Ripes
finden Sie unter “Help - System calls” eine Tabelle der unterst ̈utzten environment calls.
1 . data
2 s t r : . s t r i n g ”CAPSLOCK”
3 n e w l i n e : . s t r i n g ” \n”
4 . t e x t
5 l i t0 , 8 # number o f c h a r s
6 l a a1 , s t r # l o a d a d d r e s s o f s t r i n a1
7 mv a2 , a1 # copy a1 c o n t e n t i n t o a2
8 add a3 , a2 , t 0 # a3 <− l a s t a d d r e s s o f s t r
9 p r i n t l o o p : l b a0 , 0 ( a2 ) # l o a d c o n t e n t o f memory [ a1 +0] i n t o a0
10 l i a7 11 # code f o r p r i n t i n g a c h a r
11 e c a l l # environment c a l l
12 a d d i a2 , a2 , 1 # a2 <− a2 + 1
13 bne a2 , a3 , p r i n t l o o p # i f ( a2 != a3 ) g o t o p r i n t l o o p
14 l i a7 , 4 # code f o r p r i n t i n g s t r i n g
15 l a a0 , n e w l i n e
16 e c a l l
17
18 . . . # Your code h e r e
19
20 l i a7 , 10 # e x i t code
21 e c a l l
```

```riscv
.data
  str: .string "CAPSLOCK"
  newline: .string "\n"
.text
  li t0, 8               # number of chars
  la a1, str             # load address of string in a1
  mv a2, a1              # copy a1 content into a2
  add a3, a2, t0         # a3 <- last address of str
printloop:  lb a0, 0(a2) # load content of memory[a1+0] into a0
            li a7, 11    # code for printing a char
            ecall        # environment call
            addi a2, a2, 1 # a2 <- a2 + 1
            bne a2, a3, printloop # if (a2 != a3) goto printloop
            li a7, 4     # code for printing string
            la a0, newline
            ecall

            # Your code here

            li a7, 10    # exit code
            ecall
```

Now modify the code to convert the string to lowercase.

```riscv
.data
  str: .string "CAPSLOCK"
  newline: .string "\n"
.text
  li t0, 8               # number of chars
  la a1, str             # load address of string in a1
  mv a2, a1              # copy a1 content into a2
  add a3, a2, t0         # a3 <- last address of str
printloop:  lb a0, 0(a2) # load content of memory[a1+0] into a0
            li a7, 11    # code for printing a char
            ecall        # environment call
            addi a2, a2, 1 # a2 <- a2 + 1
            bne a2, a3, printloop # if (a2 != a3) goto printloop
            li a7, 4     # code for printing string
            la a0, newline
            ecall

            mv a2, a1
loop:       lb a0, 0(a2) # load content of memory[a1+0] into a0
            addi a0, a0, 32 # a0 <- a0 + 32
            sb a0, 0(a2) # store a0 in memory[a1+0]
            addi a2, a2, 1 # a2 <- a2 + 1
            bne a2, a3, loop # if (a2 != a3) goto loop
            li a7, 4     # code for printing string
            la a0, str
            ecall
            li a7, 4     # code for printing string
            la a0, newline
            ecall

            li a7, 10    # exit code
            ecall
```

---

Aufgabe 4 (Sternchengrafik)
Auf der Konsole soll folgendes Muster erscheinen

```text
  **
 ****
******
```

Die Zeilenanzahl (1-9) soll dabei durch eine Eingabe  ̈uber die Tastatur bestimmt werden.
Eingaben außerhalb des Parameterbereichs sollen abgelehnt werden. Die Grafik soll dabei
immer am linken Rand erscheinen.

```riscv
.data
prompt1: .string "\nEnter number of lines (1-9): "
message1: .string "\nInvalid input. Please try again.\n"
buffer:  .zero 1
oneChar: .string "1"
nineChar: .string "9"
newline: .string "\n"
space: .string " "
star: .string "*"
currSpace: .zero 4 # int
currStar: .zero 4 # int


.text
start:
li a7, 63 # read
li a0, 0  # stdin
la a1, buffer
li a2, 1  # read 1 byte
ecall

# we should have a number in buffer[0]
# check if it is in range
li t0, 49 # 1
li t1, 57 # 9
la t2, buffer
lb t2, 0(t2) # load buffer[0] into t2
# if correct, go to check2
bge t2, t0, check2 # if (t2 >= t0) goto check2, so i >= 1
# if not, go to error
j error

check2:
# if correct, go to check3
ble t2, t1, check3 # if (t2 <= t1) goto check3, so i <= 9
# if not, go to error
j error

check3:
# Try to print this.
# we'll use printRepeat (a0 = char, a1 = count)
la t0, buffer
lb t0, 0(t0) # load buffer[0] into t0
sub t0, t2, t0 # t0 = t2 - t0
li t1, 1 # t1 = 1
# write t0 spaces, then t1 stars, then t1 stars, then newline
lineLoop:
la a0, space
mv a1, t0
call printRepeat
la a0, star
mv a1, t1
call printRepeat
call printRepeat
la a0, newline
li a7, 4 # print string
# save t0 in currSpace
la t2, currSpace
sw t0, 0(t2)
# save t1 in currStar
la t2, currStar
sw t1, 0(t2)
ecall
# restore
lw t0, currSpace
lw t1, currStar
# decrement t0
addi t0, t0, -1
# increment t1
addi t1, t1, 2
bne t0, x0, lineLoop
j end

printRepeat:
# a0 = char, a1 = count
# save t0, t1
la t2, currSpace
sw t0, 0(t2)
la t2, currStar
sw t1, 0(t2)
# save arguments
mv t0, a0
mv t1, a1
# print a1 times a0
printLoop:
mv a0, t0
li a7, 4 # print string
ecall
addi t1, t1, -1
bne t1, x0, printLoop
# restore t0, t1
lw t0, currSpace
lw t1, currStar
ret

end:
li a7, 10 # exit
ecall

error:
la a0, message1
li a7, 4 # print string
ecall
```
