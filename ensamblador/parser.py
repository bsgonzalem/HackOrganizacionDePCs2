
class Parser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        instructions = []

        with open(self.file_path, "r", encoding="utf-8") as source_file:
            for line_number, original_line in enumerate(source_file, start=1):

                instruction = original_line.split("//", 1)[0]
                instruction = instruction.replace(" ", "").replace("\t", "").strip()

                if instruction:
                    instructions.append((line_number, instruction))

        return instructions
