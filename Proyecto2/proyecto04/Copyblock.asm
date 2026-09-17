@R0
D=M
@where
M=D

@R1
D=M
@there
M=D

@R2
D=M 
@count
M=D

(LOOP)

    @count
    D=M
    @END
    D;JEQ

    @where
    A=M
    D=M

    @there
    A=M
    M=D

    @there
    M=M+1

    @where
    M=M+1

    @count
    M=M-1

    @LOOP
    0;JMP

(END)
@END
0;JMP