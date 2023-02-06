from Csomag import Csomag


def beolvasas():
    fajlom = open("csomag.txt", "r", encoding="utf-8")
    fejlec = fajlom.readline()
    sorok = fajlom.readlines()
    fajlom.close()
    return sorok

def feldolgozas(sorok):
    csomag_lista = []
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("#")
        csomag_lista.append(Csomag(sor))
        i += 1
    return csomag_lista


def poggyaszok_szama(lista):
    poggyasszam = len(lista)
    return poggyasszam


def poggyaszok_atlag_sulya(lista, szelesseg):
    i = 0
    csomagszam = 0
    ossz_suly = 0
    while i < len(lista):
        if lista[i].szelesseg == szelesseg:
            csomagszam += 1
            ossz_suly += lista[i].suly
        i += 1
    atlag_suly_grammban = int(ossz_suly / csomagszam * 1000)
    return atlag_suly_grammban


def legmagasabb_poggyasz(lista):
    i = 0
    magassag = 0
    legmagasabb_helye = 0
    while i < len(lista):
        if lista[i].magassag > magassag:
            magassag = lista[i].magassag
            legmagasabb_helye = i
        i += 1
    print(f"III/D:\n\tA legmagasabb poggyász méretei: {lista[legmagasabb_helye].szelesseg}x{lista[legmagasabb_helye].magassag}x{lista[legmagasabb_helye].melyseg}, súlya: {lista[legmagasabb_helye].suly} kg.")
