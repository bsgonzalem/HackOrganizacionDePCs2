import re

from ensamblador.parser import Parser
from ensamblador.symbol_table import SymbolTable
from ensamblador.code import Code


class Assembler:

    SYMBOL_PATTERN = r"^[A-Za-z_.$:][A-Za-z0-9_.$:]*$"

    def __init__(self, file_path):
        self.file_path = file_path
        self.parser = Parser(file_path)
        self.symbol_table = SymbolTable()
        self.instructions = []
        self.errors = []

    def assemble(self):
        self.instructions = self.parser.parse()

        self.first_pass()
        machine_code = self.second_pass()

        if self.errors:
            self.errors.sort(key=lambda error: error[0])
            line_number, message = self.errors[0]
            raise ValueError(f"ERROR *** Línea {line_number}: {message}")

        return machine_code

    def first_pass(self):
        instruction_address = 0

        for line_number, instruction in self.instructions:

            if instruction.startswith("(") or instruction.endswith(")"):
                self._process_label(
                    instruction,
                    line_number,
                    instruction_address
                )
            else:
                instruction_address += 1

    def _process_label(self, instruction, line_number, address):
        if not (instruction.startswith("(") and instruction.endswith(")")):
            self.errors.append(
                (line_number, "Definición de etiqueta inválida.")
            )
            return

        symbol = instruction[1:-1]

        if not re.fullmatch(self.SYMBOL_PATTERN, symbol):
            self.errors.append(
                (line_number, "Nombre de etiqueta inválido.")
            )
            return

        if self.symbol_table.contains(symbol):
            self.errors.append(
                (line_number, f"Etiqueta duplicada o símbolo predefinido: {symbol}.")
            )
            return

        self.symbol_table.add_entry(symbol, address)

    def second_pass(self):
        machine_code = []

        for line_number, instruction in self.instructions:

            if instruction.startswith("(") or instruction.endswith(")"):
                continue

            try:
                if instruction.startswith("@"):
                    binary_instruction = self._translate_a_instruction(instruction)
                else:
                    binary_instruction = self._translate_c_instruction(instruction)

                machine_code.append(binary_instruction)

            except ValueError as error:
                self.errors.append((line_number, str(error)))

        return machine_code

    def _translate_a_instruction(self, instruction):
        symbol = instruction[1:]

        if not symbol:
            raise ValueError("Instrucción A sin valor.")

        if symbol.isdigit():
            address = int(symbol)

            if address > 32767:
                raise ValueError("La dirección A debe estar entre 0 y 32767.")

        elif re.fullmatch(self.SYMBOL_PATTERN, symbol):
            if self.symbol_table.contains(symbol):
                address = self.symbol_table.get_address(symbol)
            else:
                address = self.symbol_table.add_variable(symbol)

        else:
            raise ValueError("Símbolo o dirección A inválida.")

        return format(address, "016b")

    def _translate_c_instruction(self, instruction):
        destination = ""
        jump = ""

        if instruction.count("=") > 1 or instruction.count(";") > 1:
            raise ValueError("Instrucción C con separadores inválidos.")

        if "=" in instruction:
            destination, instruction = instruction.split("=", 1)

            if not destination:
                raise ValueError("Destino vacío en instrucción C.")

        if ";" in instruction:
            operation, jump = instruction.split(";", 1)

            if not jump:
                raise ValueError("Salto vacío en instrucción C.")
        else:
            operation = instruction

        if not operation:
            raise ValueError("Operación vacía en instrucción C.")

        operation_code = Code.get_operation_code(operation)
        destination_code = Code.get_destination_code(destination)
        jump_code = Code.get_jump_code(jump)

        return "111" + operation_code + destination_code + jump_code
