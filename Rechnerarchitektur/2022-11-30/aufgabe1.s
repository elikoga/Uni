#Aufgabe 1 (Sequentielle Multiplikation)
# Schreiben Sie ein Programm, welches 2 Zahlen einliest, diese multipliziert und das Er-
# gebnis anschließend ausgibt. Die Operanden seien 2 ganzzahlige, positive 16-Bit Zahlen.
# Implementieren Sie einen Algorithmus der maximal 16 Additionen und logische Operato-
# ren benutzt (Der Multiplikationsbefehl des RISC-V soll nicht verwendet werden).

.data
    num1: .half 0x0100
    num2: .half 0x0010

.text
start:

read:
# TODO, read num1 and num2 from stdin
# Leave unchanged for now

mult:
li t0, 0x00000000 # t0 is our result
lh t1, num1 # t1 is our first operand
lh t2, num2 # t2 is our second operand
li t3, 16 # t3 is our counter
li t4, 0x00000001 # t4 is our mask

loop:
# do if t2 & t4 == 0, then we don't add anything
and t5, t2, t4 # t5 is our last bit of t2
beqz t5, skip # skip if t2 & t4 == 0
add t0, t0, t1 # t0 += t1
skip:
# shift t1 to the left
slli t1, t1, 1
# shift t2 to the right
srli t2, t2, 1
# decrement t3
addi t3, t3, -1
# check if t3 == 0
bnez t3, loop # if t3 != 0, loop again

write:
# opcode 36 is PrintIntUnsigned
li a7, 36
mv a0, t0
ecall

