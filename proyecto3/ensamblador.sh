if [ "$#" -ne 1 ]; then
    echo "Uso: ./ensamblador.sh archivo.asm"
    exit 1
fi

INPUT_FILE="$1"

if [ ! -f "$INPUT_FILE" ]; then
    echo "ERROR: El archivo de entrada no existe."
    exit 1
fi

OUTPUT_FILE="${INPUT_FILE%.*}.hack"

python -c "
import sys
from ensamblador.ensamblador import Assembler

try:
    assembler = Assembler(sys.argv[1])
    machine_code = assembler.assemble()

    with open(sys.argv[2], 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(machine_code) + '\n')

except (ValueError, OSError) as error:
    print(error, file=sys.stderr)
    sys.exit(1)
" "$INPUT_FILE" "$OUTPUT_FILE"

if [ "$?" -ne 0 ]; then
    exit 1
fi

echo "Ensamblado completado: $OUTPUT_FILE"
