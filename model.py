import random

#konstante
ZACETEK = "Z"

NAPACEN_VNOS = "0"

ZMAGA_1 = "W1"
ZMAGA_2 = "W2"
REMI = "R"

SIRINA = 7
VISINA = 6

    
#plosca je visine 6 in sirine 7
def def_plosce():
    plosca = []
    vrstica = []
    for i in range(SIRINA):
        vrstica.append("")
    for i in range(VISINA):
        plosca.append(vrstica)
    return plosca



class Igra:

    def __init__(self, plosca, igralec):
        self.plosca = plosca
        self.igralec = igralec



    def simbol_pade_do_konca(self, izbira_stolpca):
        v = VISINA - 1
        s = int(izbira_stolpca) - 1
        while self.plosca[v][s] != "":
            v -= 1
        if v < 0:
            return NAPACEN_VNOS
        elif self.igralec == True:
            self.igralec = False
            self.plosca[v][s] = "O"
            return self.plosca
        else:
            self.igralec = True
            self.plosca[v][s] = "X"
            return self.plosca



    def poteza_racunalnika(self):
        return random.randint(1, SIRINA)


    def zmaga_O(self):
        # vodoravno
        for v in range(VISINA):      # v = vrstica in s = stolpec
            for s in range(SIRINA - 3):
                if self.plosca[v][s] == "O" and self.plosca[v][s + 1] == "O" and self.plosca[v][s + 2] == "O" and self.plosca[v][s + 3] == "O":
                    return True
        # navpicno
        for v in range(VISINA - 3):
            for s in range(SIRINA):
                if self.plosca[v][s] == "O" and self.plosca[v + 1][s] == "O" and self.plosca[v + 2][s] == "O" and self.plosca[v + 3][s] == "O":
                    return True
        # posevno /
        for v in range(VISINA - 3):
            for s in range(SIRINA - 3):
                if self.plosca[v][s] == "O" and self.plosca[v + 1][s + 1] == "O" and self.plosca[v + 2][s + 2] == "O" and self.plosca[v + 3][s + 3] == "O":
                    return True
        # posevno \
        for v in range(VISINA - 3):
            for s in reversed(range(SIRINA - 3)):
                if self.plosca[v][s + 3] == "O" and self.plosca[v + 1][s + 2] == "O" and self.plosca[v + 2][s + 1] == "O" and self.plosca[v + 3][s] == "O":
                    return True
        return False

    def zmaga_X(self):
                # vodoravno
        for v in range(VISINA):      # v = vrstica in s = stolpec
            for s in range(SIRINA - 3):
                if self.plosca[v][s] == "X" and self.plosca[v][s + 1] == "X" and self.plosca[v][s + 2] == "X" and self.plosca[v][s + 3] == "X":
                    return True
        # navpicno
        for v in range(VISINA - 3):
            for s in range(SIRINA):
                if self.plosca[v][s] == "X" and self.plosca[v + 1][s] == "X" and self.plosca[v + 2][s] == "X" and self.plosca[v + 3][s] == "X":
                    return True
        # posevno /
        for v in range(VISINA - 3):
            for s in range(SIRINA - 3):
                if self.plosca[v][s] == "X" and self.plosca[v + 1][s + 1] == "X" and self.plosca[v + 2][s + 2] == "X" and self.plosca[v + 3][s + 3] == "X":
                    return True
        # posevno \
        for v in range(VISINA - 3):
            for s in reversed(range(SIRINA - 3)):
                if self.plosca[v][s + 3] == "X" and self.plosca[v + 1][s + 2] == "X" and self.plosca[v + 2][s + 1] == "X" and self.plosca[v + 3][s] == "X":
                    return True
        return False



    def poteza(self, izbira_stolpca):
        if self.igralec == True:         #to ni racunalnik
            self.plosca = self.simbol_pade_do_konca(izbira_stolpca)
            return self.plosca
        else:                             #igra racunalnik
            self.plosca = self.simbol_pade_do_konca(self.poteza_racunalnika())
            return self.plosca



    def narisi_plosco(self):
        for v in self.plosca:
            print(v)


def nova_igra():
    plosca = def_plosce()
    igralec = random.choice([True, False])
    return Igra(plosca, igralec)

