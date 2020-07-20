import model

def izpis_poraza(igra):
    return "IZGUBIL SI, več sreče prihodnjič!"

def izpis_zmage(igra):
    return "ZMAGAL SI!"

def izpis_igre(igra):
    text = ( igra.narisi_plosco() )
    return text

def zahtevaj_vnos():
    return input("Izberi stolpec:")

def pozeni_vmesnik():
    # Naredimo novo igro
    trenutna_igra = model.nova_igra()

    while True:
        #pokazemo mu stanje
        print(izpis_igre(trenutna_igra))

        izbira_stolpca = zahtevaj_vnos()

        rezultat = trenutna_igra.poteza(izbira_stolpca)

        if trenutna_igra.zmaga_O():
            print(izpis_zmage(trenutna_igra))
            return #koncas
        if trenutna_igra.zmaga_X():
            print(izpis_poraza(trenutna_igra))
            return #koncas

pozeni_vmesnik()
