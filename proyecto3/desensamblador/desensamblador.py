from desensamblador.parser import Parser
from desensamblador.code import Code


class Disassembler:

    def __init__(self, file_path):
        self.file_path = file_path
        self.parser = Parser(file_path)

    def disassemble(self):
        instructions = self.parser.parse()
        decoded_instructions = []

        for line_number, instruction in instructions:
            try:
                decoded_instruction = self._translate_instruction(instruction)
                decoded_instructions.append(decoded_instruction)

            except ValueError as error:
                raise ValueError(
                    f"ERROR *** Línea {line_number}: {error}"
                )

        return self._generate_labels(decoded_instructions)

    def _translate_instruction(self, instruction):

        # Instrucción A
        if instruction.startswith("0"):
            address = int(instruction[1:], 2)

            return {
                "type": "A",
                "value": address,
                "assembly": f"@{address}",
                "jump": ""
            }

        # Instrucción C
        if instruction.startswith("111"):
            binary_operation = instruction[3:10]
            binary_destination = instruction[10:13]
            binary_jump = instruction[13:16]

            operation = Code.get_operation(binary_operation)
            destination = Code.get_destination(binary_destination)
            jump = Code.get_jump(binary_jump)

            assembly = operation

            if destination:
                assembly = destination + "=" + assembly

            if jump:
                assembly += ";" + jump

            return {
                "type": "C",
                "value": None,
                "assembly": assembly,
                "jump": jump
            }

        raise ValueError("Código de instrucción inválido.")

    def _generate_labels(self, instructions):

        instruction_count = len(instructions)
        target_addresses = set()

        # Identificar las direcciones de destino
        for index in range(1, instruction_count):

            current_instruction = instructions[index]
            previous_instruction = instructions[index - 1]

            if current_instruction["type"] != "C":
                continue

            if not current_instruction["jump"]:
                continue

            if previous_instruction["type"] != "A":
                continue

            target_address = previous_instruction["value"]

            if target_address <= instruction_count:
                target_addresses.add(target_address)

        # Asignar etiquetas en orden de dirección
        labels = {
            address: f"L{index}"
            for index, address in enumerate(sorted(target_addresses))
        }

        # Sustituir las direcciones A por etiquetas
        for index in range(1, instruction_count):

            current_instruction = instructions[index]
            previous_instruction = instructions[index - 1]

            if (
                current_instruction["type"] == "C"
                and current_instruction["jump"]
                and previous_instruction["type"] == "A"
            ):

                target_address = previous_instruction["value"]

                if target_address in labels:
                    previous_instruction["assembly"] = (
                        f"@{labels[target_address]}"
                    )

        # Construir el programa ensamblador
        assembly_program = []

        for index in range(instruction_count + 1):

            if index in labels:
                assembly_program.append(f"({labels[index]})")

            if index < instruction_count:
                assembly_program.append(
                    instructions[index]["assembly"]
                )

        return assembly_program
