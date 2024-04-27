from kocka import Kocka
from zvire import Zvire
from kachna import Kachna

zvire = Zvire(10, "průhledná")
kachna = Kachna(2, "bílá")
kocka = Kocka(8, "Hnědá")


farma = [zvire, kachna, kocka]

for zvire in farma:
    print(zvire.mluv())





















"""
from clovek import Clovek
from programator import Programator
from python_programator import PythonProgramator

cecil = Clovek("Cecil", 20)
pepa = Programator("Pepa", 35, "Heslo123")
petr = Programator("Petr", 20, "Heslo456")
pavel = PythonProgramator("Pavel", 50, "Heslo789", "3.9.11")
#               0     1      2     3
spolecnost = [cecil, pepa, petr, pavel]

for clovek  in spolecnost:
    clovek.pozdrav()

for clovek in spolecnost:
    print(clovek)


"""