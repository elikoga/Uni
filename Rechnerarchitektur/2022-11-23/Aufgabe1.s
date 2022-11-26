# Aufgabe1.s
#
        .data                   # start data section
answer: .string "Result = "
argument: .word   5

        .text                   # start text section
main:   lw  a0, argument   		# Load argument from static data
        addi t0, a0, 0     		# load 5 into t0
        addi t1, zero, 1
        and  t2, t2, zero

loop:   beqz  t0,  done
        add  t2, t2, t1
        addi  t0, t0, -1
        slli  t1, t1, 1
        j    loop

done:   la a0, answer          	# load address of string into a0
        li a7, 4                # code for printing string
        ecall
        mv a0, t2               # move result to a0
        li a7, 36               # code for printing an unsigned integer
        ecall
        li a7, 10               # load environment call code for exit
        ecall
