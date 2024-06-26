class Nakladak:

    def __init__(self, nosnost, naklad = 0):
        self._nosnost = nosnost
        self._naklad = naklad


    def naloz(self, mnozstvi):
        #  kolik vezeme + kolik chceme naložit <= max nosnost
        if self._naklad + mnozstvi <= self._nosnost:
            self._naklad += mnozstvi
        else:
            raise Exception("Překročena maximální nosnost!")

    def vyloz(self, mnozstvi):
        # to, co chci vyložit <= kolik vezeme
        if mnozstvi <= self._naklad:
            self._naklad -= mnozstvi
        else:
            raise Exception("Nedostatek nákladu pro vyložení!")

    def vypis(self):
        print(f"Vezu {self._naklad} kg nákladu.")

    def bogus(self):
        try:
            return 1
        except Exception as e:
            return 2
        finally:
            return 3