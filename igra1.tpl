% import model1

  <h1>Štiri v vrsto</h1>

  <blockquote>
    Projektna naloga pri predmetu UVP - 1. letnik.
    <p><small>Avtor: <bold>Urban Rupnik</bold></small></p>
  </blockquote>


  <style type="text/css">
  .tg  {width: 70% ; height: 350px; table-layout: fixed; text-align: center; vertical-align: bottom; padding: 0%; border-collapse:collapse;border-color:#9ABAD9;border-spacing:0;}
  .tg td{background-color:#EBF5FF;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#444;
    font-family:Arial, sans-serif;font-size:14px;font-weight: normal; overflow:auto;padding:0%;word-break:normal;table-layout: fixed;}
  .tg th{background-color:#409cff;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#fff;
    font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:auto;padding:0%;word-break:normal;table-layout: fixed;}
  .tg .tg-empm{font-family:Arial, sans-serif !important;;font-size:14px;font-weight: normal; text-align:center;vertical-align:bottom;padding: 0%;table-layout: fixed;}
  </style>
  <table class="tg">
  <thead>
    <tr>
      <th class="tg-s8il">1</th>
      <th class="tg-jq8f">2</th>
      <th class="tg-jq8f">3</th>
      <th class="tg-jq8f">4</th>
      <th class="tg-jq8f">5</th>
      <th class="tg-jq8f">6</th>
      <th class="tg-jq8f">7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="tg-s8il">{{igra.vrstica0()[0]}}</td>
      <td class="tg-jq8f">{{igra.vrstica0()[1]}}</td>
      <td class="tg-jq8f">{{igra.vrstica0()[2]}}</td>
      <td class="tg-jq8f">{{igra.vrstica0()[3]}}</td>
      <td class="tg-jq8f">{{igra.vrstica0()[4]}}</td>
      <td class="tg-jq8f">{{igra.vrstica0()[5]}}</td>
      <td class="tg-jq8f">{{igra.vrstica0()[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.vrstica1()[0]}}</td>
      <td class="tg-jq8f">{{igra.vrstica1()[1]}}</td>
      <td class="tg-jq8f">{{igra.vrstica1()[2]}}</td>
      <td class="tg-jq8f">{{igra.vrstica1()[3]}}</td>
      <td class="tg-jq8f">{{igra.vrstica1()[4]}}</td>
      <td class="tg-jq8f">{{igra.vrstica1()[5]}}</td>
      <td class="tg-jq8f">{{igra.vrstica1()[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.vrstica2()[0]}}</td>
      <td class="tg-jq8f">{{igra.vrstica2()[1]}}</td>
      <td class="tg-jq8f">{{igra.vrstica2()[2]}}</td>
      <td class="tg-jq8f">{{igra.vrstica2()[3]}}</td>
      <td class="tg-jq8f">{{igra.vrstica2()[4]}}</td>
      <td class="tg-jq8f">{{igra.vrstica2()[5]}}</td>
      <td class="tg-jq8f">{{igra.vrstica2()[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.vrstica3()[0]}}</td>
      <td class="tg-jq8f">{{igra.vrstica3()[1]}}</td>
      <td class="tg-jq8f">{{igra.vrstica3()[2]}}</td>
      <td class="tg-jq8f">{{igra.vrstica3()[3]}}</td>
      <td class="tg-jq8f">{{igra.vrstica3()[4]}}</td>
      <td class="tg-jq8f">{{igra.vrstica3()[5]}}</td>
      <td class="tg-jq8f">{{igra.vrstica3()[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.vrstica4()[0]}}</td>
      <td class="tg-jq8f">{{igra.vrstica4()[1]}}</td>
      <td class="tg-jq8f">{{igra.vrstica4()[2]}}</td>
      <td class="tg-jq8f">{{igra.vrstica4()[3]}}</td>
      <td class="tg-jq8f">{{igra.vrstica4()[4]}}</td>
      <td class="tg-jq8f">{{igra.vrstica4()[5]}}</td>
      <td class="tg-jq8f">{{igra.vrstica4()[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.vrstica5()[0]}}</td>
      <td class="tg-jq8f">{{igra.vrstica5()[1]}}</td>
      <td class="tg-jq8f">{{igra.vrstica5()[2]}}</td>
      <td class="tg-jq8f">{{igra.vrstica5()[3]}}</td>
      <td class="tg-jq8f">{{igra.vrstica5()[4]}}</td>
      <td class="tg-jq8f">{{igra.vrstica5()[5]}}</td>
      <td class="tg-jq8f">{{igra.vrstica5()[6]}}</td>
    </tr>
  </tbody>
  </table>

  % if poskus == "W":
    <h1> ZMAGAL SI! </h1>
  % elif poskus == "L":
    <h1> IZGUBIL SI! </h1>
    <h2> Več sreče prihodnjič!</h2>
  % elif poskus == "R":
    <h1> NEODLOČENO</h1>
    <h2> Poskusi še enkrat!</h2>

  % elif igra.igralec == True:

  <form action="/igra/{{id_igre}}/" method="post">
    Izbira stolpca: <input type="number" min="1" max="7" name="izbira_stolpca" required>
    <button type="submit">Izberi</button>
  </form>

  % else:
  
  <form action="/igra/{{id_igre}}/" method="post">
    Poteza računalnika: <input type="hidden" name="izbira_stolpca">
    <button type="submit">Klikni</button>
  </form>
  
  % end

  
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>