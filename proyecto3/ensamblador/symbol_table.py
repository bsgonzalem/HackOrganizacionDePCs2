class SymbolTable:

    def __init__(self):
        self.symbols = {}
        self.variable_address = 16

        self._add_predefined_symbols()

    def _add_predefined_symbols(self):
        predefined_symbols = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576
        }

        for symbol, address in predefined_symbols.items():
            self.add_entry(symbol, address)

        for register_number in range(16):
            self.add_entry(f"R{register_number}", register_number)

    def add_entry(self, symbol, address):
        self.symbols[symbol] = address

    def contains(self, symbol):
        return symbol in self.symbols

    def get_address(self, symbol):
        return self.symbols[symbol]

    def add_variable(self, symbol):
        if not self.contains(symbol):

            if self.variable_address > 32767:
                raise ValueError("No hay direcciones disponibles para nuevas variables.")

            self.add_entry(symbol, self.variable_address)
            self.variable_address += 1

        return self.get_address(symbol)
