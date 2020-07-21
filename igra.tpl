% import model
% import tekstovni_vmesnik
% rebase("datoteke/views/base.tpl")
% trenutna_igra = model.nova_igra()
  <h1>Štiri v vrsto</h1>

  <blockquote>
    Projektna naloga pri predmetu Uvod v programiranje - 1. letnik.
    <p><small>Avtor: <bold>Urban Rupnik</bold></small></p>
  </blockquote>

  <h2> {{ izpis_igre(trenutna_igra) }} </h2>

  

  % if trenutna_igra.zmaga_O() == True:
    <h1> ZMAGAL SI </h1>
  % elif trenutna_igra.zmaga_X() == True:
    <h1> IZGUBIL SI </h1>
    <h2> Več sreče prihodnjič!</h2>
  % else:
  

  <form action="/igra/" method="post">
    Izbira stolpca: <input type="text" name="izberi_stolpec">
    <button type="submit">Izberi</button>
  </form>

  % end

  
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>