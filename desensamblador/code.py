class Code:

    OPERATION_TABLE = {
        "0101010": "0",
        "0111111": "1",
        "0111010": "-1",
        "0001100": "D",
        "0110000": "A",
        "1110000": "M",
        "0001101": "!D",
        "0110001": "!A",
        "1110001": "!M",
        "0001111": "-D",
        "0110011": "-A",
        "1110011": "-M",
        "0011111": "D+1",
        "0110111": "A+1",
        "1110111": "M+1",
        "0001110": "D-1",
        "0110010": "A-1",
        "1110010": "M-1",
        "0000010": "D+A",
        "1000010": "D+M",
        "0010011": "D-A",
        "1010011": "D-M",
        "0000111": "A-D",
        "1000111": "M-D",
        "0000000": "D&A",
        "1000000": "D&M",
        "0010101": "D|A",
        "1010101": "D|M"
    }

    DESTINATION_TABLE = {
        "000": "",
        "001": "M",
        "010": "D",
        "011": "MD",
        "100": "A",
        "101": "AM",
        "110": "AD",
        "111": "AMD"
    }

    JUMP_TABLE = {
        "000": "",
        "001": "JGT",
        "010": "JEQ",
        "011": "JGE",
        "100": "JLT",
        "101": "JNE",
        "110": "JLE",
        "111": "JMP"
    }

    @classmethod
    def get_operation(cls, binary_operation):
        if binary_operation not in cls.OPERATION_TABLE:
            raise ValueError("Código de operación inválido.")

        return cls.OPERATION_TABLE[binary_operation]

    @classmethod
    def get_destination(cls, binary_destination):
        if binary_destination not in cls.DESTINATION_TABLE:
            raise ValueError("Código de destino inválido.")

        return cls.DESTINATION_TABLE[binary_destination]

    @classmethod
    def get_jump(cls, binary_jump):
        if binary_jump not in cls.JUMP_TABLE:
            raise ValueError("Código de salto inválido.")

        return cls.JUMP_TABLE[binary_jump]
