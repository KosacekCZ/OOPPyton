class Zvire:

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

    def mluv(self):
        return ""

    def vypis(self):
        return f"Jsem zvíře, vážím {self.vaha} kg, mám barvu {self.barva} a {self.get_leta()}"

    def __str__(self):
        return f"{self.barva}, {self.vaha}"