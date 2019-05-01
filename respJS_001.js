function Q1() {
    console.log('Q1');
    var x = Number.parseInt(document.getElementById('x').value);
    var y = Number.parseInt(document.getElementById('y').value);
    console.log ('X / Y:' + x + '/' + y);
    console.log ('Quociente = ' + Math.floor (x/y));
    console.log ('Resto = ' + (x%y));
}


function Q2() {
    console.log('Q2');
    var x = Number.parseFloat(document.getElementById('cateto1').value);
    var y = Number.parseFloat(document.getElementById('cateto2').value);
    console.log (x)
    console.log (y)
    console.log (Math.sqrt (Math.pow (x,2) + (Math.pow (y,2))));
}

function Q3() {
    console.log('Q3');
    var aux = document.getElementById('profissoes');
    var profissao = aux.options[aux.selectedIndex].value ;
    if (profissao == 'musicista' || profissao == 'presidente')
        {console.log ('Ambos')}
    else {
        if ( profissao.endsWith('a') || profissao.endsWith('iz'))
            {console.log ('Feminino')}
        if ( profissao.endsWith('o') || profissao.endsWith('or'))
            {console.log ('Masculino')}
    }
    
}


function Q4() {
    console.log('Q4');
    var a_str = document.getElementById("a").value;
    var b_str = document.getElementById("b").value;
    var c_str = document.getElementById("c").value;
    if ( (c_str) === '')
        {console.log (Math.sqrt ((Math.pow (a_str,2) + Math.pow (b_str,2))));}
    if ( (a_str) === '')
        {console.log (Math.sqrt (Math.pow (c_str,2) - Math.pow (b_str,2))); }
    if ( (b_str) === '')
        {console.log (Math.sqrt (Math.pow (c_str,2) - Math.pow (a_str,2))); }
}

function Q5() {
    console.log('Q5');
    var altura = Number.parseFloat(document.getElementById('altura').value);
    var massa = Number.parseFloat(document.getElementById('massa').value);
    var aux = document.getElementById('generos');
    var genero = aux.options[aux.selectedIndex].value;
    imc =(massa/(altura*altura));

    
    if (genero == 'masculino1')
    {if (imc < 18.5 )
        {console.log ('Magro')}
        else { if (imc >= 18.5 && imc < 24.9)
                {console.log ('Sarado')}
                else {if (imc >= 25 && imc < 29.9)
                    {console.log ('Rechonchudo')}
                    else {if (imc > 30)
                        {console.log ('Obeso')}}}}}
    else {{if (imc < 18.5 )
        {console.log ('Magra')}
        else { if (imc >= 18.5 && imc < 24.9)
                {console.log ('Sarada')}
                else {if (imc >= 25 && imc < 29.9)
                    {console.log ('Rechonchuda')}
                    else {if (imc > 30)
                        {console.log ('Obesa')}}}}}}
}