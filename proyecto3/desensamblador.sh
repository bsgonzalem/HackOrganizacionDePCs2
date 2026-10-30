if [ "$#" -ne 1 ]; then
    echo "Uso: ./desensamblador.sh archivo.hack"
    exit 1
fi

INPUT_FILE="$1"

if [ ! -f "$INPUT_FILE" ]; then
    echo "ERROR: El archivo de entrada no existe."
    exit 1
fi

DIRECTORY=$(dirname "$INPUT_FILE")
FILENAME=$(basename "$INPUT_FILE" .hack)
OUTPUT_FILE="$DIRECTORY/${FILENAME}Dis.asm"

python -c "
import sys
from desensamblador.desensamblador import Disassembler

try:
    disassembler = Disassembler(sys.argv[1])
    assembly_code = disassembler.disassemble()

    with open(sys.argv[2], 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(assembly_code) + '\n')

except (ValueError, OSError) as error:
    print(error, file=sys.stderr)
    sys.exit(1)
" "$INPUT_FILE" "$OUTPUT_FILE"

if [ "$?" -ne 0 ]; then
    exit 1
fi

echo "Desensamblado completado: $OUTPUT_FILE"
