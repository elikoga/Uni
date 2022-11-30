# Aufgabe 2 (Fibonacci-Folge)
# Schreiben Sie ein Assemblerprogramm, das die ersten n Fibonacci-Zahlen ausgibt. Die
# Fibonacci-Zahlen sind durch folgende rekursive Bildungsvorschrift bestimmt:
# F (n) = F (n − 1) + F (n − 2); F (0) = 0; F (1) = 1
# (1) Legen Sie hierzu zun ̈achst die Fibonacci-Zahlen auf den Stack und geben Sie diese
# dann in absteigender Reihenfolge aus.
# (2) Welche Nachteile sehen Sie in dieser Implementierung und wie k ̈onnte die Funktion
# effizienter implementiert werden?

.data
n: .word 10
newline: .string "\n"

.text
addi sp, sp, -8 # Reserve space for 0 and 1
sw zero, 0(sp)
li t0, 1
sw t0, 4(sp)

la t5, n
lw t5, 0(t5) # i
calculateLoop:
lw t0, 0(sp) # F_n-1
lw t1, 4(sp) # F_n-2
add t2, t0, t1 # F_n
addi sp, sp, -4 # Reserve space for F_n
sw t2, 0(sp) # Push F_n
addi t5, t5, -1 # i--
bnez t5, calculateLoop # if i != 0 goto loop

la t6 n
lw t6, 0(t6) # n
li t5, 1 # i
printLoop:
lw a0, 0(sp) # F_n
li a7, 36
ecall
la a0, newline
li a7, 4 # print string
ecall
addi sp, sp, 4 # Pop F_n
addi t5, t5, 1 # i++
bne t5, t6, printLoop # if i != n goto loop

li a7, 10
ecall