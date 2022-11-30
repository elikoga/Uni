# Aufgabe 3 (Binomialkoeffizient)
# In dieser Aufgabe sollen zwei Implementierungen zur Berechnung der Binomialkoeffizien-
# ten verglichen werden.
# (1) Schreiben Sie ein Programm zur Berechnung von n!. Erweitern Sie das Programm
# dahingehend, dass eine Zahl n durch z.b.
# argument n : .word 2
# eingelesen, n! berechnet und anschließend ausgegeben wird. Verwenden Sie dazu die
# Programmteile (Eingabe, Ausgabe) aus den Programmen der vorherigen  ̈Ubungs-
# aufgaben.
# (2) Schreiben Sie ein Programm, welches (n# k# ) mit Hilfe der Fakult ̈atsfunktion berechnet.
# (3) Die Binomialkoeffizienten sind rekusiv wie folgt definiert:
# Schreiben Sie ein Programm, welches (n# k# ) rekursiv berechnet.
# (4) Vergleichen Sie die beiden implementierten Programme zur Berechnung der Binomi-
# alkoeffizienten. Der Ripes Simulator hat unter Processor eine Schaltfl ̈ache Execution
# info mit dem Feld Instrs. retired. Wie viele Instruktionen braucht jedes Programm
# f ̈ur die Berechnung von (10# 5# )? F ̈ur welches maximale n k ̈onnen alle Binomialkoef-
# fizienten mit den jeweiligen Programmen berechnet werden? Stellen Sie daf ̈ur die
# Ungleichungen auf und sch ̈atzen Sie n ab.

.data
argument_n: .word 10

.text
main:
li t0, 1 # 1 is the monoid identity of multiplication
li t1, 1 # 1 is the monoid identity of multiplication, termination condition
la t2, argument_n # load address of argument_n into t2
lw t2, 0(t2) # load value of argument_n into t2
loop:
mul t0, t0, t2 # multiply t0 with t2
addi t2, t2, -1 # decrement t2
bne t2, t1, loop # branch if t2 is not equal to t1

output:
li a7, 36 # system call number for print integer
mv a0, t0 # move t0 into a0
ecall # print t0