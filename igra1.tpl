% import model1

  <h1>Štiri v vrsto</h1>

  <blockquote>
    Projektna naloga pri predmetu Uvod v programiranje - 1. letnik.
    <p><small>Avtor: <bold>Urban Rupnik</bold></small></p>
  </blockquote>

  <h2> {{ igra.plosca1() }} </h2>


  % if poskus == "W":
    <h1> ZMAGAL SI </h1>
  % elif poskus == "L":
    <h1> IZGUBIL SI </h1>
    <h2> Več sreče prihodnjič!</h2>
  % else:

  <form action="/igra/" method="post">
    Izbira stolpca: <input type="text" name="izbira_stolpca">
    <button type="submit">Izberi</button>
  </form>
  
  % end

  
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>