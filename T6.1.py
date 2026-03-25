import random


# Parametriton funktio, joka palauttaa satunnaisen luvun väliltä 1–6
def heita_noppaa():
    return random.randint(1, 6)


# Pääohjelma
while True:
    silmaluku = heita_noppaa()
    print(silmaluku)

    if silmaluku == 6:
        break