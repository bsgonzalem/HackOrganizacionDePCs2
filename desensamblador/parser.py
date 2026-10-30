class Parser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        instructions = []

        with open(self.file_path, "r", encoding="utf-8") as source_file:

            for line_number, original_line in enumerate(source_file, start=1):

                instruction = original_line.strip()

                if len(instruction) != 16:
                    raise ValueError(
                        f"ERROR *** Línea {line_number}: "
                        "La instrucción debe contener exactamente 16 bits."
                    )

                if any(bit not in "01" for bit in instruction):
                    raise ValueError(
                        f"ERROR *** Línea {line_number}: "
                        "La instrucción contiene caracteres diferentes de 0 y 1."
                    )

                if instruction[0] == "1" and not instruction.startswith("111"):
                    raise ValueError(
                        f"ERROR *** Línea {line_number}: "
                        "Prefijo de instrucción C inválido."
                    )

                instructions.append((line_number, instruction))

        return instructions
