@res
M=0

@R1
D=M

@STOP
D;JEQ

(LOOP)

    @R0
    D=M

    @res
    M=D+M

    @R1
    M=M-1

    @R1
    D=M

    @LOOP
    D;JGT

(STOP)

    @res
    D=M

    @R2
    M=D

    @STOP
    0;JMP