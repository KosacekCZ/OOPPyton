from programator import Programator

class PythonProgramator(Programator):

    def __init__(self, jmeno, vek, heslo, verze_pythonu):
        super().__init__(jmeno, vek, heslo)
        self.verze_pythonu = verze_pythonu

    def pozdrav(self, zpusob_pozdravu = "Ahoj"):
        print(f"{self.jmeno}@{self.verze_pythonu}> {zpusob_pozdravu}, já jsem {self.jmeno}, programuju v pythonu!")