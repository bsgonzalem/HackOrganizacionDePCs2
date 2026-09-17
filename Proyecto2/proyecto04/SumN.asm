@resultado
M=0

@i
M=1

(SUM)

@i
D=M
@R0
D=D-M
@STOP
D;JGT

@i
D=M
@resultado
D=D+M
@resultado
M=D

@i
M=M+1

@SUM
0;JMP

(STOP)

@resultado
D=M
@R1
M=D