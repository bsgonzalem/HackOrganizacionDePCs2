# Informe técnico – Proyecto 3: Ensamblador y Desensamblador Hack

## 1. Introducción

Para este proyecto se solicitó desarrollar un ensamblador y un desensamblador para la plataforma Hack, capaces de convertir archivos en lenguaje ensamblador (`.asm`) a código binario (`.hack`) y viceversa.

Para su desarrollo se tomó como base un proyecto anterior del curso de Lenguajes Formales y Compiladores, denominado RuleBased. Este proyecto tenía una estructura muy similar, ya que también se centraba en el procesamiento de un lenguaje, la interpretación de sus instrucciones y la validación de su sintaxis. Por esta razón, sirvió como una referencia importante para el proyecto, tanto en su organización como en la manera de analizar y procesar las instrucciones.

## 2. Estructura del proyecto

El proyecto se divide en dos módulos principales: `ensamblador` y `desensamblador`. Cada uno contiene sus archivos de código y se encarga de una parte específica del proceso de traducción.

También se cuenta con una carpeta de pruebas, los scripts para ejecutar los programas y los archivos de documentación.

Esto con base a la recomendación del proyecto.

## 3. Ensamblador

El ensamblador convierte las instrucciones Hack a código binario de 16 bits. Para esto utiliza dos iteraciones:

- **Primera iteracion:** identifica las etiquetas del programa y registra sus direcciones en la tabla de símbolos.
- **Segunda iteracion:** traduce las instrucciones A y C a su representación binaria, asignando direcciones a las variables cuando es necesario.

La tabla de símbolos permite reconocer nombres predefinidos, etiquetas y variables utilizadas en el programa.

## 4. Desensamblador

El desensamblador recibe archivos `.hack` y convierte cada instrucción binaria en su equivalente en lenguaje ensamblador.

Primero valida que las instrucciones tengan el formato correcto y después interpreta sus bits para identificar el tipo de instrucción, la operación, el destino y el salto.

También implementa la generación de etiquetas para las instrucciones de salto, siguiendo la regla establecida en el enunciado.

## 5. Manejo de errores

Ambos programas cuentan con validaciones para detectar instrucciones incorrectas.

El ensamblador identifica errores relacionados con direcciones, etiquetas, destinos, operaciones, saltos y estructura de las instrucciones.

El desensamblador detecta errores de longitud, caracteres inválidos, prefijos incorrectos y códigos de operación no reconocidos.

Los errores se muestran indicando el número de línea donde se encuentran.

## 6. Pruebas y resultados

Se desarrollaron pruebas para los dos programas, incluyendo archivos válidos y casos con errores.

Las pruebas del ensamblador permitieron comprobar la traducción de instrucciones y el manejo de símbolos. Las pruebas del desensamblador permitieron verificar la interpretación de las instrucciones binarias y la generación de etiquetas.

También se comprobó que, al desensamblar un archivo y volver a ensamblar el resultado, se obtiene el mismo código binario original.

## 7. Integrante

- Brayan Santiago González Mateus


## 9. Conclusiones

El desarrollo del proyecto permitió comprender cómo se traducen las instrucciones entre lenguaje ensamblador y código máquina. También permitió trabajar con tablas de símbolos, validación de instrucciones, manejo de errores y generación de etiquetas.

Las pruebas permitieron comprobar el funcionamiento de ambos programas y verificar que se conserva el código binario durante el proceso de traducción inversa.