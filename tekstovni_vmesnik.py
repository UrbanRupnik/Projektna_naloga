import model1

def izpis_poraza(igra):
    return "IZGUBIL SI, več sreče prihodnjič!"

def izpis_zmage(igra):
    return "ZMAGAL SI!"

def izpis_remija(igra):
    return "NEODLOČENO, poskusi še enkrat!"

def izpis_igre(igra):
    presledek = "-----------------------------------"
    igra.narisi_plosco()
    print(presledek)

def zahtevaj_vnos():
    return input("Izberi stolpec:")

def pozeni_vmesnik():
    # Naredimo novo igro
    trenutna_igra = model1.nova_igra()

    while True:
        #pokazemo mu stanje
        izpis_igre(trenutna_igra)

        if trenutna_igra.igralec == True:
            izbira_stolpca = zahtevaj_vnos()
            
        else:
            izbira_stolpca = trenutna_igra.poteza_racunalnika()


        rezultat = trenutna_igra.poteza(izbira_stolpca)

        izpis_igre(trenutna_igra)

        if trenutna_igra.zmaga_O():
            print(izpis_zmage(trenutna_igra))
            return #koncas
        if trenutna_igra.zmaga_X():
            print(izpis_poraza(trenutna_igra))
            return #koncas
        if trenutna_igra.remi():
            print(izpis_remija(trenutna_igra))
            return #koncas

pozeni_vmesnik()
