# Práctica 2 - Construcción de la Plataforma Hack: Lenguaje Máquina, CPU y Computador

Docente: José Luis Montoya Pareja.

## Organización de Computadores


El objetivo de este proyecto es implementar diferentes programas en lenguaje ensamblador Hack y construir los componentes principales de la plataforma Hack: Memory, CPU y Computer.

El proyecto está basado en los Proyectos 4 y 5 de Nand2Tetris.

## Contenido del proyecto

### Proyecto 4 - Programas en ensamblador

- `Mult.asm`: realiza la multiplicación de dos números mediante sumas repetidas.
- `Fill.asm`: permite llenar o limpiar la pantalla dependiendo de si se presiona una tecla.
- `SumN.asm`: calcula la suma de los primeros N números naturales.
- `CopyBlock.asm`: copia un bloque de datos de una posición de memoria a otra.

### Proyecto 5 - Hardware

- `Memory.hdl`: implementa la memoria del computador Hack, incluyendo RAM, pantalla y teclado.
- `CPU.hdl`: implementa la CPU encargada de ejecutar las instrucciones.
- `Computer.hdl`: integra la CPU, la memoria y la ROM para formar el computador Hack completo.

## Funcionamiento general

Mediante Nand2Tetris nos permite simular los componentes del hardware y como se comportan, a su vez nos permite desde assembler ver procesos mucho mas internos de como actuan los procesos basicos de los mismos. 

En la parte de hardware, la CPU recibe las instrucciones desde la ROM y se comunica con la memoria para leer y escribir datos.

## Tecnologías utilizadas

- Nand2Tetris Plataforma donde se crearon los proyectos
- Logisim Plataforma para poder recrear el hardware y facilitarme la contruscción en hack
- Codex Corrección y Explicación de errores
- Git Manejo de proyecto
- Visual Studio Code IDE

## Estructura del proyecto

├── proyecto04/
│   ├── HDL
│   ├── DOCUMENTACION
│   └── TESTS
│
├── proyecto05/
│   ├── HDL
│   ├── DOCUMENTACION
│   └── TESTS
│
└── README.md

