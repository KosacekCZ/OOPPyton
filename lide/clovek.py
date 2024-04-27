class Clovek:
    __konto = 0

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.__vek = vek
        self.__cislo_karty = "1234 5678 9101 1121"



    def stav_konta(self):
        return Clovek.__konto

    def vklad(self, castka):
        Clovek.__konto += castka

    @staticmethod
    def inflace(mira):
        Clovek.__konto *= mira



    def pozdrav(self, zpusob_pozdravu = "Ahoj"):
        print(f"{zpusob_pozdravu}, já jsem {self.jmeno}")




    # Property - dělá z metod "atributy / proměnné" (stejná práce s nimi, nevoláme jako metody)

    @property
    def vek(self):
        return self.__vek

    @vek.setter
    def vek(self, novy_vek):
        if novy_vek > 0:
            self.__vek = novy_vek

    def get_cislo_karty(self):
        return f"**** **** **** {self.__cislo_karty[15:19]}"

    def __str__(self):
        return f"{self.jmeno}"

    def __eq__(self, other):
        if self.jmeno == other.jmeno:
            return True