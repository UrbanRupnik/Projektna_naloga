% import model1

  <h1>Štiri v vrsto</h1>

  <blockquote>
    Projektna naloga pri predmetu Uvod v programiranje - 1. letnik.
    <p><small>Avtor: <bold>Urban Rupnik</bold></small></p>
  </blockquote>

  <h2> <p>{{ igra.vrstica0() }}</p>
       <p>{{ igra.vrstica1() }}</p> 
       <p>{{ igra.vrstica2() }}</p>
       <p>{{ igra.vrstica3() }}</p>
       <p>{{ igra.vrstica4() }}</p>
       <p>{{ igra.vrstica5() }}</p> </h2>


  % if poskus == "W":
    <h1> ZMAGAL SI </h1>
  % elif poskus == "L":
    <h1> IZGUBIL SI </h1>
    <h2> Več sreče prihodnjič!</h2>
  % elif poskus == "R":
    <h1> NEODLOČENO</h1>
    <h2> Poskusi še enkrat!</h2>

  % else:

  <form action="/igra/{{id_igre}}/" method="post">
    Izbira stolpca: <input type="number" name="izbira_stolpca">
    <button type="submit">Izberi</button>
  </form>
  
  % end

  
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>