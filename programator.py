from clovek import Clovek

class Programator(Clovek):

    def __init__(self, jmeno, vek, heslo):
        super().__init__(jmeno, vek)
        self.heslo = heslo

    def pozdrav(self, zpusob_pozdravu = "Ahoj"):
        print(f"{zpusob_pozdravu}, já jsem {self.jmeno}, je mi {self.vek}, a hash mého hesla je {hash(self.heslo)}")

    def __str__(self):
        return super().__str__() + f"{self.heslo}"