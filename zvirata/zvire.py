from abc import ABC, abstractmethod


class Zvire(ABC):

    def __init__(self, vaha, barva):
        self.vaha = vaha
        self.barva = barva

    def nakrm(self, mnozstvi):
        self.vaha += mnozstvi

    def get_leta(self):
        if self.vaha < 9:
            return "létám"
        else:
            return "nelétám"

    @abstractmethod
    def mluv(self)->str:
        pass

    def __str__(self):
        return f"{self.barva}, {self.vaha}"