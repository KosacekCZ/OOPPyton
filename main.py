from lide.clovek import Clovek

bob = Clovek("Bob", 25)
alice = Clovek("Alice", 30)

bob.vklad(5000)
alice.vklad(10000)

print(bob.stav_konta())
print(alice.stav_konta())

Clovek.inflace(0.85)

print(bob.stav_konta())
print(alice.stav_konta())












"""
příklad lambda
jmena = ["Adam", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet"]

jmena2 = list(filter(lambda jmeno: len(jmeno) < 4, jmena))

print(jmena2)
"""

# příklad na Enum, barvičky
#kacka = Kachna(2, Barvy.BILA)
#print(kacka.barva.value)

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