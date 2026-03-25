import random


# Funktio saa parametrina tahkojen lukumäärän
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


# Pääohjelma
tahkot = int(input("Anna nopan tahkojen määrä: "))

while True:
    silmaluku = heita_noppaa(tahkot)
    print(silmaluku)

    if silmaluku == tahkot:
        break