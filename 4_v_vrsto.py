import bottle

import model

stiri = model.Stiri()
trenutna_igra = model.nova_igra()


@bottle.get("/")
def index():
    return bottle.template("datoteke/views/index.tpl")

@bottle.post("/igra/")
def nova_igra():
    id_nove_igre = stiri.nova_igra()
    bottle.redirect(f"/igra/{id_nove_igre}/")


@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    igra, poskus = stiri.igre[id_igre]

    return bottle.template("datoteke/views/igra.tpl", igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post("/igra/<id_igre:int>/")
def igranje(id_igre):
    
    izbira_stolpca = bottle.request.forms.getunicode("izbira_stolpca")

    stiri.igranje(id_igre, izbira_stolpca)

    bottle.redirect(f"/igra/{id_igre}/")


bottle.run(reloader=True, debug=True) 