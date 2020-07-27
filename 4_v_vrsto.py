import bottle
import model1

stiri = model1.Stiri()


@bottle.get("/")
def index():
    return bottle.template("index1.tpl")


@bottle.post("/igra/")
def nova_igra():
    id_nove_igre = stiri.nova_igra()
    bottle.redirect(f"/igra/{id_nove_igre}/")


@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    igra, poskus = stiri.igre[id_igre]
    return bottle.template("igra1.tpl", igra=igra, poskus=poskus, id_igre=id_igre)


@bottle.post("/igra/<id_igre:int>/")
def igranje(id_igre):    
    izbira_stolpca = bottle.request.forms.getunicode("izbira_stolpca")
    stiri.igranje(id_igre, izbira_stolpca)
    bottle.redirect(f"/igra/{id_igre}/")


bottle.run(reloader=True, debug=True) 