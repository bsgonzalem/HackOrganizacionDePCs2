# Proyecto 3 – Ensamblador y Desensamblador Hack

## 1. Descripción del proyecto

En este proyecto se solicito crear un ensamblador y un desensamblador para traducir de asemble a hack y viceversa, sus funciones son las siguientes:

- **Ensamblador:** traduce programas escritos en lenguaje ensamblador Hack (`.asm`) a código binario (`.hack`).
- **Desensamblador:** traduce programas en código binario Hack (`.hack`) a instrucciones en lenguaje ensamblador (`.asm`).

## 2. Requerimeintos 

- Python 3.14.3 o una versión compatible.
- Git Bash en Windows para ejecutar los scripts `.sh`.
- No se requieren dependencias externas de Python.

## 3. Estructura del proyecto (al usar el proyecto tree /F)

```text
proyecto3/
│
├── compilar.sh
├── ensamblador.sh
├── desensamblador.sh
├── README.md
│
├── ensamblador/
│   ├── ensamblador.py
│   ├── code.py
│   ├── parser.py
│   ├── symbol_table.py
│   └── __init__.py
│
├── desensamblador/
│   ├── desensamblador.py
│   ├── code.py
│   ├── parser.py
│   └── __init__.py
│
├── pruebas/
│   ├── ensamblador/
│   │   ├── definidas/
│   │   └── validas/
│   ├── desensamblador/
│   │   ├── definidas/
│   │   └── validas/
│   ├── errores/
│   │   ├── ensamblador/
│   │   └── desensamblador/
│   └── README.md
│
└── DOCUMENTACION/
    └── INFORME.md
```

## 4. Instalación y configuración

1. Descargar o clonar el repositorio.
2. Abrir una terminal Git Bash en la carpeta raíz del proyecto (`proyecto3/`).
3. Ejecutar el script de compilación:

```bash
./compilar.sh
```

## 5. Compilación y ejecución

Todos los comandos deben ejecutarse desde la carpeta raíz `proyecto3/`, utilizando Git Bash.

### 5.1. Ensamblador

Para convertir un archivo `.asm` a `.hack`:

```bash
./ensamblador.sh ruta/al/archivo.asm
```

Ejemplo:

```bash
./ensamblador.sh pruebas/ensamblador/definidas/Prueba1.asm
```

El archivo `.hack` resultante se genera en la misma carpeta del archivo de entrada y conserva su nombre base.

### 5.2. Desensamblador

Para convertir un archivo `.hack` a `.asm`:

```bash
./desensamblador.sh ruta/al/archivo.hack
```

Ejemplo:

```bash
./desensamblador.sh pruebas/desensamblador/definidas/Prueba3.hack
```

El archivo `.asm` resultante se genera en la misma carpeta del archivo de entrada, agregando el sufijo `Dis` al nombre base.

### 5.3. Ejecución de las pruebas

Las pruebas están organizadas en las carpetas `pruebas/ensamblador/`, `pruebas/desensamblador/` y `pruebas/errores/`.

Para ejecutar una prueba del ensamblador:

```bash
./ensamblador.sh pruebas/ensamblador/validas/prueban1.asm
```

Para ejecutar una prueba del desensamblador:

```bash
./desensamblador.sh pruebas/desensamblador/validas/prueban1d.hack
```

Para ejecutar los casos de error del ensamblador:

```bash
for f in pruebas/errores/ensamblador/*/*.asm; do
    ./ensamblador.sh "$f"
done
```

Para ejecutar los casos de error del desensamblador:

```bash
for f in pruebas/errores/desensamblador/*/*.hack; do
    ./desensamblador.sh "$f"
done
```