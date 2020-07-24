import random
import json

#konstante
ZACETEK = "Z"


ZMAGA = "W"
PORAZ = "L"
REMI = "R"

SIRINA = 7
VISINA = 6


#plosca je visine 6 in sirine 7
def def_plosce():
    vrstica = []
    for i in range(SIRINA):
        vrstica.append(" ")
    plosca = [vrstica for j in range(VISINA)]
    return plosca



class Igra:

    def __init__(self, plosca, igralec):
        self.plosca = plosca
        self.igralec = igralec



    def simbol_pade_do_konca(self, izbira_stolpca):
        if int(izbira_stolpca) > 7 or int(izbira_stolpca) < 1: #napacen vnos, izbira se enkrat isti igralec
            return self.plosca
        a = 0
        nova_vrstica = []
        nova_plosca = []
        v = VISINA - 1
        s = int(izbira_stolpca) - 1
        while self.plosca[v][s] != " ":
            v -= 1
            if v < 0:
                break
        if v < 0:
            return self.plosca #poln stolpec, izbira se enkrat isti igralec
        elif self.igralec == True:
            self.igralec = False
            for vrstica in self.plosca:
                if a == v:
                    for znak in vrstica:
                        nova_vrstica.append(znak)
                    nova_vrstica[s] = "O"
                    vrstica = nova_vrstica
                nova_plosca.append(vrstica)
                a += 1
            self.plosca = nova_plosca
            return self.plosca
        else:
            self.igralec = True
            for vrstica in self.plosca:
                if a == v:
                    for znak in vrstica:
                        nova_vrstica.append(znak)
                    nova_vrstica[s] = "X"
                    vrstica = nova_vrstica
                nova_plosca.append(vrstica)
                a += 1
            self.plosca = nova_plosca
            return self.plosca



    def poteza_racunalnika(self):
        if self.skorajX_vod() != False:
            return self.skorajX_vod()

        if self.skorajX_nav() != False:
            return self.skorajX_nav()

        if self.skorajX_pos1() != False:
            return self.skorajX_pos1()
            
        if self.skorajX_pos2() != False:
            return self.skorajX_pos2()

        if self.skoraj_vod() != False:
            return self.skoraj_vod()


        if self.skoraj_nav() != False:
            return self.skoraj_nav()

        if self.skoraj_pos1() != False:
            return self.skoraj_pos1()
            
        if self.skoraj_pos2() != False:
            return self.skoraj_pos2()
        
        else:
            return random.randint(1, SIRINA)  
                

    def skoraj_vod(self): # vodoravno
        for v in range(VISINA):      # v = vrstica in s = stolpec
            for s in range(SIRINA - 2):
                if self.plosca[v][s] == "O" and self.plosca[v][s + 1] == "O" and self.plosca[v][s + 2] == "O":
                    if self.plosca[v][s - 1] == " " or self.plosca[v][s + 3] == " ":
                        if v == 5: # prva vrstica
                            if s - 1 >= 0 and self.plosca[v][s - 1] == " ":
                                return s
                            if  s + 3 <= 6 and self.plosca[v][s + 3] == " ":
                                return s + 4
                            else:
                                return False
                        if v <= 4:
                            if s - 1 >= 0 and self.plosca[v][s - 1] == " " and self.plosca[v + 1][s - 1] != " ":
                                return s
                            if  s + 3 <= 6 and self.plosca[v][s + 3] == " " and self.plosca[v + 1][s + 3] != " ":
                                return s + 4
                            else:
                                return False
        return False

    def skoraj_nav(self):    # navpicno
        for v in range(VISINA - 2):
            for s in range(SIRINA):
                if self.plosca[v][s] == "O" and self.plosca[v + 1][s] == "O" and self.plosca[v + 2][s] == "O":
                    if self.plosca[v - 1][s] == " ":
                        return s + 1
        return False

    def skoraj_pos1(self):    # posevno \
        for v in range(VISINA - 2):
            for s in range(SIRINA - 2):
                if self.plosca[v][s] == "O" and self.plosca[v + 1][s + 1] == "O" and self.plosca[v + 2][s + 2] == "O":
                    if v >= 1 and s >= 1 and self.plosca[v - 1][s - 1] == " " and self.plosca[v][s - 1] != " ":
                        return s
                    if v <= 1 and s <= 3 and self.plosca[v + 3][s + 3] == " " and self.plosca[v + 4][s + 3] != " ":
                        return s + 4      
        return False
    
    def skoraj_pos2(self):    # posevno /
        for v in range(VISINA - 2):
            for s in reversed(range(SIRINA - 2)):
                if self.plosca[v][s + 2] == "O" and self.plosca[v + 1][s + 1] == "O" and self.plosca[v + 2][s] == "O":
                    if v >= 1 and s <= 3 and self.plosca[v - 1][s + 3] == " " and self.plosca[v][s + 3] != " ":
                        return s + 4
                    if v <= 1 and s >= 1 and self.plosca[v + 3][s - 1] == " " and self.plosca[v + 4][s - 1] != " ":
                        return s
        return False


    def skorajX_vod(self): # vodoravno zmaga za X
        for v in range(VISINA):      # v = vrstica in s = stolpec
            for s in range(SIRINA - 2):
                if self.plosca[v][s] == "X" and self.plosca[v][s + 1] == "X" and self.plosca[v][s + 2] == "X":
                    if self.plosca[v][s - 1] == " " or self.plosca[v][s + 3] == " ":
                        if v == 5: # prva vrstica
                            if s - 1 >= 0 and self.plosca[v][s - 1] == " ":
                                return s
                            if  s + 3 <= 6 and self.plosca[v][s + 3] == " ":
                                return s + 4
                            else:
                                return False
                        if v <= 4:
                            if s - 1 >= 0 and self.plosca[v][s - 1] == " " and self.plosca[v + 1][s - 1] != " ":
                                return s
                            if s + 3 <= 6 and self.plosca[v][s + 3] == " " and self.plosca[v + 1][s + 3] != " ":
                                return s + 4
                            else:
                                return False
        return False

    def skorajX_nav(self):    # navpicno
        for v in range(VISINA - 2):
            for s in range(SIRINA):
                if self.plosca[v][s] == "X" and self.plosca[v + 1][s] == "X" and self.plosca[v + 2][s] == "X":
                    if self.plosca[v - 1][s] == " ":
                        return s + 1
        return False

    def skorajX_pos1(self):    # posevno \
        for v in range(VISINA - 2):
            for s in range(SIRINA - 2):
                if self.plosca[v][s] == "X" and self.plosca[v + 1][s + 1] == "X" and self.plosca[v + 2][s + 2] == "X":
                    if v >= 1 and s >= 1 and self.plosca[v - 1][s - 1] == " " and self.plosca[v][s - 1] != " ":
                        return s
                    if v <= 1 and s <= 3 and self.plosca[v + 3][s + 3] == " " and self.plosca[v + 4][s + 3] != " ":
                        return s + 4     
        return False
    
    def skorajX_pos2(self):    # posevno /
        for v in range(VISINA - 2):
            for s in reversed(range(SIRINA - 2)):
                if self.plosca[v][s + 2] == "X" and self.plosca[v + 1][s + 1] == "X" and self.plosca[v + 2][s] == "X":
                    if v >= 1 and s <= 3 and self.plosca[v - 1][s + 3] == " " and self.plosca[v][s + 3] != " ":
                        return s + 4
                    if v <= 1 and s >= 1 and self.plosca[v + 3][s - 1] == " " and self.plosca[v + 4][s - 1] != " ":
                        return s
        return False

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

        # posevno \
        for v in range(VISINA - 3):
            for s in range(SIRINA - 3):
                if self.plosca[v][s] == "O" and self.plosca[v + 1][s + 1] == "O" and self.plosca[v + 2][s + 2] == "O" and self.plosca[v + 3][s + 3] == "O":
                    return True

        # posevno /
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

    def remi(self):
        for v in self.plosca:
            for znak in v:
                if znak == " ":
                    return False
        return True


    def poteza(self, izbira_stolpca):
        if self.igralec == True:         #to ni racunalnik
            self.plosca = self.simbol_pade_do_konca(izbira_stolpca)
            return self.plosca
        else:                             #igra racunalnik
            self.plosca = self.simbol_pade_do_konca(izbira_stolpca)
            return self.plosca

    def vrstica0(self):
        return self.plosca[0]
    def vrstica1(self):
        return self.plosca[1]
    def vrstica2(self):
        return self.plosca[2]    
    def vrstica3(self):
        return self.plosca[3]
    def vrstica4(self):
        return self.plosca[4]
    def vrstica5(self):
        return self.plosca[5]

    def narisi_plosco(self):
        for v in self.plosca:
            print(v)


    def igranje(self, izbira_stolpca):
        if self.igralec == True:
            self.plosca = self.simbol_pade_do_konca(izbira_stolpca)
            if self.zmaga_O():
                return ZMAGA
            if self.remi():
                return REMI
        else:
            izbira_stolpca = self.poteza_racunalnika()
            self.plosca = self.simbol_pade_do_konca(izbira_stolpca)
            if self.zmaga_X():
                return PORAZ
            if self.remi():
                return REMI


def nova_igra1():
    plosca = def_plosce()
    igralec = random.choice([True, False])
    return Igra(plosca, igralec)


class Stiri:
    def __init__(self):
        # Slovar, ki ID-ju priredi objekt igre
        self.igre = {}    # int -> (Igra, stanje)

    def prosti_id_igre(self):  # vrne nov id, ki ga neuporablja se nobena igra
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        # dobimo svež id
        nov_id = self.prosti_id_igre()

        # naredimo novo igro
        sveza_igra = nova_igra1()

        # vse to shranimo v self.igre
        self.igre[nov_id] = sveza_igra, ZACETEK

        # vrnemo nov id
        return nov_id

    def igranje(self, id_igre, izbira_stolpca):
        # dobimo staro igro ven
        trenutna_igra, _ = self.igre[id_igre]

        # igramo, dobimo novo stanje
        novo_stanje = trenutna_igra.igranje(izbira_stolpca)

        # zapisemo posodbljeno stanje in igro nazaj v "BAZO"
        self.igre[id_igre] = (trenutna_igra, novo_stanje)
