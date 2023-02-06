import random


def veletlen_generator():
    veletlen_szamok_listaja = []
    while len(veletlen_szamok_listaja) < 12:
        veletlen_szam = int(random.random() * 1012 - 11)
        veletlen_szamok_listaja.append(veletlen_szam)
    return veletlen_szamok_listaja


def kiiratas(lista, karakter):
    i = 0
    veletlen_szamok_elvalasztva = ""
    while i < len(lista) - 1:
        veletlen_szamok_elvalasztva += str(lista[i]) + str(karakter)
        i += 1
    veletlen_szamok_elvalasztva += str(lista[i])
    return veletlen_szamok_elvalasztva


def paratlanok_szama(lista):
    i = 0
    paratlan_db = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            paratlan_db += 1
        i += 1
    return paratlan_db


def konzol_kiir(ertek):
    print(f"II/D, E:\n\tA páratlanok száma: {ertek}.")


def fajlba_kiir(kiirando):
    fajlom = open("eredmeny.txt", "w", encoding="utf-8")
    fajlom.write(str(kiirando))
    fajlom.close()