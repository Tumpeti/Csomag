class Csomag:
    def __init__(self, sor):
        self.szelesseg = int(sor[0])
        self.magassag = int(sor[1])
        self.melyseg = int(sor[2])
        self.suly = int(sor[3])

    def __str__(self):
        return f"{self.szelesseg}, {self.magassag}, {self.melyseg}, {self.suly}"
