lb x1, 0x10(x2)
lh x1, 0x10(x2)
lw x1, 0x10(x2)
sb x1, 0x10(x2)
sh x1, 0x10(x2)
sw x1, 0x10(x2)
add x1, x2, x3
sub x1, x2, x3
and x1, x2, x3
or x1, x2, x3
xor x1, x2, x3
addi x1, x2, 0x10
li x1, 0x10
mv x1, x2
andi x1, x2, 0x10
ori x1, x2, 0x10
sll x1, x2, x3
srl x1, x2, x3
bne x1, x2, -72
beq x1, x2, -76
blt x1, x2, -80
bge x1, x2, -84
bnez x1, -88
beqz x1, -92
bltz x1, -96
bgez x1, -100