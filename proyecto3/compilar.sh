if ! command -v python >/dev/null 2>&1; then
    echo "ERROR: Python no está instalado o no está disponible en PATH."
    exit 1
fi

python --version
