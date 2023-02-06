import ertekel
import poggyasz1
import sorozat

ertekel.bekeres()
veletlen_szamok_listaja = sorozat.veletlen_generator()
print(f"II/A, B, C:\n\t{(sorozat.kiiratas(veletlen_szamok_listaja,'$'))}")
# print(f"II/F:\n\tA páratlanok száma: {sorozat.paratlanok_szama(veletlen_szamok_listaja)}")
sorozat.konzol_kiir(sorozat.paratlanok_szama(veletlen_szamok_listaja))
sorozat.fajlba_kiir(f"II/F:\n\tA páratlanok száma: {sorozat.paratlanok_szama(veletlen_szamok_listaja)}")

poggyasz_lista = poggyasz1.feldolgozas(poggyasz1.beolvasas())
print(f"III/A, B:\n\tA poggyászok száma: {poggyasz1.poggyaszok_szama(poggyasz_lista)}")
print(f"III/C:\n\tAz 51 cm-es poggyászok átlag súlyértéke: {poggyasz1.poggyaszok_atlag_sulya(poggyasz_lista, szelesseg=51)}g")
poggyasz1.legmagasabb_poggyasz(poggyasz_lista)