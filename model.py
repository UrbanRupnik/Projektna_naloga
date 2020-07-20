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


    def poteza(self, izbira_stolpca):
        if self.igralec == True:         #to ni racunalnik
            return simbol_pade_do_konca(izbira_stolpca)
        else:                             #igra racunalnik
            return simbol_pade_do_konca(poteza_racunalnika())


    def simbol_pade_do_konca(self, izbira_stolpca):
        v = VISINA - 1
        s = izbira_stolpca - 1
        while self.plosca[v][s] != "":
            v -= 1
        if v < 0:
            return NAPACEN_VNOS
        elif self.igralec == True:
            self.igralec = False
            return self.plosca[v][s] = "O"
        else:
            self.igralec = True
            return self.plosca[v][s] = "X"



    def poteza_racunalnika(self):
        return random.randint(1, SIRINA)



def nova_igra():
    plosca = def_plosce()
    igralec = random(True, False)
    return Igra(plosca, igralec)

