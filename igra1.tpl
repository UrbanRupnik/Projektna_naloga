% import model1
  <body style="background-color: #EBF5FF; font-family: Roboto, sans-serif;">
    <h1 style="background-color: #409cff ; padding-left: 20px; padding-top: 5px;">
      Štiri v vrsto</h1>

    <blockquote>
      <p>Projektna naloga pri predmetu UVP - 1. letnik.<br>
      <small>Avtor: Urban Rupnik</small><br></p>
    </blockquote>


    <style type="text/css">
    .tg  {width: 70%; height: 60%; table-layout: fixed; text-align: center;
          border-collapse: collapse; border-color: #9ABAD9;
          border-spacing: 0; font-size: 14px; overflow: auto; border-style: solid;
          border-width: 4px; word-break: normal;}
    .tg td{background-color: #EBF5FF; border-color: #9ABAD9; color: #444; 
           font-weight: bolder; padding: 2px; border-style: solid; border-width: 4px;}
    .tg th{background-color: #409cff; border-color: #9ABAD9;
           color: #fff; border-style: solid; border-width: 4px;}
    .tg .tg-empm{padding: 0px;}
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
      <td class="tg-s8il">{{igra.narisi_vrstico(0)[0]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(0)[1]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(0)[2]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(0)[3]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(0)[4]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(0)[5]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(0)[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.narisi_vrstico(1)[0]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(1)[1]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(1)[2]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(1)[3]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(1)[4]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(1)[5]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(1)[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.narisi_vrstico(2)[0]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(2)[1]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(2)[2]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(2)[3]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(2)[4]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(2)[5]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(2)[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.narisi_vrstico(3)[0]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(3)[1]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(3)[2]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(3)[3]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(3)[4]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(3)[5]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(3)[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.narisi_vrstico(4)[0]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(4)[1]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(4)[2]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(4)[3]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(4)[4]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(4)[5]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(4)[6]}}</td>
    </tr>
    <tr>
      <td class="tg-s8il">{{igra.narisi_vrstico(5)[0]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(5)[1]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(5)[2]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(5)[3]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(5)[4]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(5)[5]}}</td>
      <td class="tg-jq8f">{{igra.narisi_vrstico(5)[6]}}</td>
    </tr>
    </tbody>
    </table>

    % if poskus == "W":
      <h1> ZMAGAL SI! </h1>
    % elif poskus == "L":
      <h2> IZGUBIL SI! <br>
       Več sreče prihodnjič! </h2>
    % elif poskus == "R":
      <h1> NEODLOČENO</h1>
      <h2> Poskusi še enkrat!</h2>

    % elif igra.igralec == True:

    <form action="/igra/{{id_igre}}/" method="post" style="padding: 1px;">
      Izbira stolpca: <input type="number" min="1" max="7" name="izbira_stolpca" 
                             required accesskey="k">
      <button type="submit">Izberi</button>
    </form>

    % else:

    <form action="/igra/{{id_igre}}/" method="post" style="padding: 1px;">
      Poteza računalnika: <input type="hidden" name="izbira_stolpca">
      <button type="submit" accesskey="k">Klikni</button>
    </form>

    % end


    <form action="/igra/" method="post">
      <button type="submit" accesskey="n">Nova igra</button>
    </form>
  </body>