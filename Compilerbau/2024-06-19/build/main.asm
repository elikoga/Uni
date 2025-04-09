
.include "/home/elikoga/Dev/Uni/Compilerbau/Assembler/framework.asm"
main:
add SP, -1
ld a, 1
ld HL, SP+0
ld (HL), a
add SP, -1
ld a, 2
ld HL, SP+0
ld (HL), a
ld HL, SP+0
ld a, (HL)
ld A, a
call printByte
add SP, 0
