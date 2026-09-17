@SCREEN
D=A
@address
M=D

(LOOP)

    @KBD
    D=M

    // si no se presiona baja a white
    @WHITE
    D;JEQ

    // coloca el negro en la pamtalla
    @address
    A=M
    M=-1

    // Suma la posición
    @address
    M=M+1

    // Verificar si terminamos la pantalla
    @address
    D=M
    @24576
    D=D-A
    @LOOP
    D;JLT
    
    // REINICIAMOS LA PANTALLA

    @SCREEN
    D=A
    @address
    M=D

    @LOOP
    0;JMP


(WHITE)

    // Pone el pixel en blanco
    @address
    A=M
    M=0

    // Suma la posición
    @address
    M=M+1

    // Verificar si terminamos la pantalla
    @address
    D=M
    @24576
    D=D-A
    @LOOP
    D;JLT

    // REINICIAMOS LA PANTALLA

    @SCREEN
    D=A
    @address
    M=D

    @LOOP
    0;JMP