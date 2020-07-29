import random

#konstante
ZACETEK = "Z"

ZMAGA = "W"
PORAZ = "L"
REMI = "R"

SIRINA = 7
VISINA = 6

# plosca je visine 6 in sirine 7
def def_plosce(): # vrne seznam seznamov velikosti igralne plosce
    vrstica = []
    for _ in range(SIRINA):
        vrstica.append(" ")
    plosca = [vrstica for j in range(VISINA)]
    return plosca


class Igra:

    def __init__(self, plosca, igralec):
        self.plosca = plosca
        self.igralec = igralec


    def napacen_vnos(self, izbira_stolpca):
        return (len(str(izbira_stolpca)) == 0 
                or int(izbira_stolpca) > 7 
                or int(izbira_stolpca) < 1)


    def simbol_pade_do_konca(self, izbira_stolpca):
        if self.napacen_vnos(izbira_stolpca):
            return self.plosca # napacen vnos, izbira se enkrat isti igralec

        v = VISINA - 1
        s = int(izbira_stolpca) - 1
        while self.plosca[v][s] != " ":
            v -= 1
            if v < 0:
                break # potuje od spodaj navzgor in se zlomi ko pride do vrha ali praznega polja
        
        if v < 0:
            return self.plosca # poln stolpec, izbira se enkrat isti igralec
        elif self.igralec == True:
            self.igralec = False
            return self.dodaj_simbol(v, s, "O")
        else:
            self.igralec = True
            return self.dodaj_simbol(v, s, "X")


    def dodaj_simbol(self, v, s, simbol):
        a = 0
        nova_vrstica = []
        nova_plosca = []
        for vrstica in self.plosca:
            if a == v:
                for znak in vrstica:
                    nova_vrstica.append(znak)
                nova_vrstica[s] = simbol
                vrstica = nova_vrstica
            nova_plosca.append(vrstica)
            a += 1
        self.plosca = nova_plosca
        return self.plosca


    def poteza_racunalnika(self):
        if self.skoraj_vod("X") != False:
            return self.skoraj_vod("X") # vrne stevilko stolpca

        elif self.skoraj_nav("X") != False:
            return self.skoraj_nav("X")

        elif self.skoraj_pos1("X") != False:
            return self.skoraj_pos1("X")
            
        elif self.skoraj_pos2("X") != False:
            return self.skoraj_pos2("X")

        elif self.skoraj_vod("O") != False:
            return self.skoraj_vod("O")

        elif self.skoraj_nav("O") != False:
            return self.skoraj_nav("O")

        elif self.skoraj_pos1("O") != False:
            return self.skoraj_pos1("O")
            
        elif self.skoraj_pos2("O") != False:
            return self.skoraj_pos2("O")
        
        else:
            return self.racunalnik_izbere_prosto_mesto(random.randint(1, SIRINA))
                

    def racunalnik_izbere_prosto_mesto(self, izbira_stolpca):
        s = izbira_stolpca - 1
        if self.plosca[0][s] == " ":
            return s + 1
        else:
            return self.racunalnik_izbere_prosto_mesto(random.randint(1, SIRINA))


    def skoraj_vod(self, simbol): # vodoravno
        for v in range(VISINA):   # v = vrstica in s = stolpec
            for s in range(SIRINA - 2):
                if self.skoraj_vod_3(simbol, v, s) != False:
                    return self.skoraj_vod_3(simbol, v, s)

                if self.skoraj_vod_1_2(simbol, v, s) != False:
                    return self.skoraj_vod_1_2(simbol, v, s)

                if self.skoraj_vod_2_1(simbol, v, s) != False:
                    return self.skoraj_vod_2_1(simbol, v, s)
        return False
    

    def skoraj_vod_3(self, simbol, v, s): # trije znaki skupaj vodoravno
        if (self.plosca[v][s] == simbol and 
            self.plosca[v][s + 1] == simbol and 
            self.plosca[v][s + 2] == simbol):
            if v == 5: # prva vrstica
                if s - 1 >= 0 and self.plosca[v][s - 1] == " ":
                    return s
                if  s + 3 <= 6 and self.plosca[v][s + 3] == " ":
                    return s + 4
            if v <= 4:
                if (s - 1 >= 0 and 
                    self.plosca[v][s - 1] == " " and 
                    self.plosca[v + 1][s - 1] != " "):
                    return s
                if (s + 3 <= 6 and 
                    self.plosca[v][s + 3] == " " and 
                    self.plosca[v + 1][s + 3] != " "):
                    return s + 4
        return False


    def skoraj_vod_1_2(self, simbol, v, s):
    # eno mesto prosto med enim in dvema znakoma (O-OO)
        if (s + 3 <= 6 and   
            self.plosca[v][s] == simbol and 
            self.plosca[v][s + 2] == simbol and 
            self.plosca[v][s + 3] == simbol):
            if (v == 5 and
                self.plosca[v][s + 1] == " "):
                    return s + 2
            if (v <= 4 and
                self.plosca[v][s + 1] == " " and 
                self.plosca[v + 1][s + 1] != " "):
                return s + 2
        return False


    def skoraj_vod_2_1(self, simbol, v, s):
    # eno mesto prosto med dvema in enim znakom (OO-O)
        if (s + 3 <= 6 and
            self.plosca[v][s] == simbol and 
            self.plosca[v][s + 1] == simbol and 
            self.plosca[v][s + 3] == simbol):
            if (v == 5 and
                self.plosca[v][s + 2] == " "):
                return s + 3
            if (v <= 4 and
                self.plosca[v][s + 2] == " " and 
                self.plosca[v + 1][s + 2] != " "):
                return s + 3
        return False


    def skoraj_nav(self, simbol):    # navpicno
        for v in range(VISINA - 2):
            for s in range(SIRINA):

                if (self.plosca[v][s] == simbol and 
                    self.plosca[v + 1][s] == simbol and 
                    self.plosca[v + 2][s] == simbol):
                    if self.plosca[v - 1][s] == " ":
                        return s + 1
        return False


    def skoraj_pos1(self, simbol):    # posevno \
        for v in range(VISINA - 2):
            for s in range(SIRINA - 2):
                if self.skoraj_pos1_trije(simbol, v, s) != False:
                    return self.skoraj_pos1_trije(simbol, v, s)

                if self.skoraj_pos1_en_dva(simbol, v, s) != False:
                    return self.skoraj_pos1_en_dva(simbol, v, s)

                if self.skoraj_pos1_dva_en(simbol, v, s) != False:
                    return self.skoraj_pos1_dva_en(simbol, v, s)
        return False
    

    def skoraj_pos1_trije(self, simbol, v, s): # trije znaki skupaj \
        if (self.plosca[v][s] == simbol and 
            self.plosca[v + 1][s + 1] == simbol and 
            self.plosca[v + 2][s + 2] == simbol):
            if (v >= 1 and 
                s >= 1 and 
                self.plosca[v - 1][s - 1] == " " and 
                self.plosca[v][s - 1] != " "):
                return s
            if (v == 2 and
                s <= 3 and
                self.plosca[v + 3][s + 3] == " "): # prva vrstica
                return s + 4
            if (v <= 1 and 
                s <= 3 and 
                self.plosca[v + 3][s + 3] == " " and 
                self.plosca[v + 4][s + 3] != " "):
                return s + 4
        return False


    def skoraj_pos1_en_dva(self, simbol, v, s):
        if (v + 3 <= 5 and   # eno mesto prosto med enim in dvema znakoma \
            s + 3 <= 6 and 
            self.plosca[v][s] == simbol and 
            self.plosca[v + 2][s + 2] == simbol and 
            self.plosca[v + 3][s + 3] == simbol):
            if (self.plosca[v + 1][s + 1] == " " and 
                self.plosca[v + 2][s + 1] != " "):
                return s + 2
        return False


    def skoraj_pos1_dva_en(self, simbol, v, s):
        if (v + 3 <= 5 and   # eno mesto prosto med dvema in enim znakom \
            s + 3 <= 6 and 
            self.plosca[v][s] == simbol and 
            self.plosca[v + 1][s + 1] == simbol and 
            self.plosca[v + 3][s + 3] == simbol):
            if (self.plosca[v + 2][s + 2] == " " and 
                self.plosca[v + 3][s + 2] != " "):
                return s + 3
        return False


    def skoraj_pos2(self, simbol):    # posevno /
        for v in range(VISINA - 2):
            for s in reversed(range(SIRINA - 2)):
                if self.skoraj_pos2_trije(simbol, v, s) != False:
                    return self.skoraj_pos2_trije(simbol, v, s)

                if self.skoraj_pos2_en_dva(simbol, v, s) != False:
                    return self.skoraj_pos2_en_dva(simbol, v, s)

                if self.skoraj_pos2_dva_en(simbol, v, s) != False:
                    return self.skoraj_pos2_dva_en(simbol, v, s)
        return False


    def skoraj_pos2_trije(self, simbol, v, s):
        if (self.plosca[v][s + 2] == simbol and  # trije znaki skupaj /
            self.plosca[v + 1][s + 1] == simbol and 
            self.plosca[v + 2][s] == simbol):
            if (v >= 1 and 
                s <= 3 and 
                self.plosca[v - 1][s + 3] == " " and 
                self.plosca[v][s + 3] != " "):
                return s + 4
            if (v == 2 and
                s >= 1 and
                self.plosca[v + 3][s - 1] == " "): # prva vrstica
                return s
            if (v <= 1 and 
                s >= 1 and 
                self.plosca[v + 3][s - 1] == " " and 
                self.plosca[v + 4][s - 1] != " "):
                return s
        return False


    def skoraj_pos2_en_dva(self, simbol, v, s):
        if (v + 3 <= 5 and   # eno mesto prosto med enim in dvema znakoma /
            s + 3 <= 6 and 
            self.plosca[v][s + 3] == simbol and 
            self.plosca[v + 2][s + 1] == simbol and 
            self.plosca[v + 3][s] == simbol):
            if (self.plosca[v + 1][s + 2] == " " and 
                self.plosca[v + 2][s + 2] != " "):
                return s + 3
        return False


    def skoraj_pos2_dva_en(self, simbol, v, s):
        if (v + 3 <= 5 and   # eno mesto prosto med dvema in enim znakom /
            s + 3 <= 6 and 
            self.plosca[v][s + 3] == simbol and 
            self.plosca[v + 1][s + 2] == simbol and 
            self.plosca[v + 3][s] == simbol):
            if (self.plosca[v + 2][s + 1] == " " and 
                self.plosca[v + 3][s + 1] != " "):
                return s + 2
        return False


    def zmaga(self, simbol):
        return (self.zmaga_vod(simbol) or
                self.zmaga_nav(simbol) or
                self.zmaga_pos1(simbol) or
                self.zmaga_pos2(simbol))


    def zmaga_vod(self, simbol):
        for v in range(VISINA):    
            for s in range(SIRINA - 3):
                if (self.plosca[v][s] == simbol and 
                    self.plosca[v][s + 1] == simbol and 
                    self.plosca[v][s + 2] == simbol and 
                    self.plosca[v][s + 3] == simbol):
                    return True
        return False


    def zmaga_nav(self, simbol):
        for v in range(VISINA - 3):
            for s in range(SIRINA):
                if (self.plosca[v][s] == simbol and 
                    self.plosca[v + 1][s] == simbol and 
                    self.plosca[v + 2][s] == simbol and 
                    self.plosca[v + 3][s] == simbol):
                    return True
        return False


    def zmaga_pos1(self, simbol): # posevno \
        for v in range(VISINA - 3):
            for s in range(SIRINA - 3):
                if (self.plosca[v][s] == simbol and 
                    self.plosca[v + 1][s + 1] == simbol and 
                    self.plosca[v + 2][s + 2] == simbol and 
                    self.plosca[v + 3][s + 3] == simbol):
                    return True
        return False


    def zmaga_pos2(self, simbol): # posevno /                
        for v in range(VISINA - 3):
            for s in reversed(range(SIRINA - 3)):
                if (self.plosca[v][s + 3] == simbol and 
                    self.plosca[v + 1][s + 2] == simbol and 
                    self.plosca[v + 2][s + 1] == simbol and 
                    self.plosca[v + 3][s] == simbol):
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


    def narisi_vrstico(self, stevilka_vrstice):
        return self.plosca[stevilka_vrstice]


    def narisi_plosco(self):  # se uporablja pri igranju v tekstovnem vmesniku
        for v in self.plosca:
            print(v)


    def igranje(self, izbira_stolpca):
        if self.igralec == True:
            self.plosca = self.simbol_pade_do_konca(izbira_stolpca)
            if self.zmaga("O"):
                return ZMAGA
            if self.remi():
                return REMI
        else:
            izbira_stolpca = self.poteza_racunalnika()
            self.plosca = self.simbol_pade_do_konca(izbira_stolpca)
            if self.zmaga("X"):
                return PORAZ
            if self.remi():
                return REMI


def nova_igra1(): # narise novo plosco in doloci kdo zacne
    plosca = def_plosce()
    igralec = random.choice([True, False])
    return Igra(plosca, igralec)


class Stiri:
    def __init__(self):
        self.igre = {}    # slovar, ki id-ju priredi objekt igre: int -> (Igra, stanje)


    def prosti_id_igre(self):  # vrne nov id, ki ga ne uporablja se nobena igra
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1


    def nova_igra(self):
        nov_id = self.prosti_id_igre() # dobimo nov id
        sveza_igra = nova_igra1() # naredimo novo igro
        self.igre[nov_id] = sveza_igra, ZACETEK # vse shranimo v self.igre
        return nov_id # vrnemo nov id


    def igranje(self, id_igre, izbira_stolpca):
        trenutna_igra, _ = self.igre[id_igre] # dobimo staro igro ven
        novo_stanje = trenutna_igra.igranje(izbira_stolpca) # igramo, dobimo novo stanje
        self.igre[id_igre] = (trenutna_igra, novo_stanje) # posodbljeno stanje in igro shranimo nazaj v self.igre
