

function EsfericaParaCartesiano(r ,phi, theta) {
    var x = r*Math.cos(theta)*Math.sin(phi);
    var y = r*Math.sin(theta)*Math.sin(phi);
    var z = r*Math.cos(phi);
    return "x=  " + x + "; y= " + y + "; z= "+ z;
}
    console.log (EsfericaParaCartesiano(1, Math.PI/3, Math.PI/6));
    console.log (EsfericaParaCartesiano(3, Math.PI/6, Math.PI/3));
    console.log (EsfericaParaCartesiano(2, Math.PI/4, Math.PI/4));

    function CalcularAreaRetangulo(lado, altura){
        return lado*altura
    }
    console.log (CalcularAreaRetangulo(7,5));




    function Q1() {
        console.log('Q1');
        var x = Number.parseInt(document.getElementById('x').value);
        var y = Number.parseInt(document.getElementById('y').value);
        console.log ('X / Y:' + x + '/' + y);
        console.log ('Quociente = ' + Math.floor (x/y));
        console.log ('Resto = ' + (x%y));
        document.getElementById('RQ1').innerHTML =DivisaoPorInteiro (x, y)
        function DivisaoPorInteiro (x, y){
        return 'X:/Y:  ' + x + '/' + y + ' ' + ' ' + 'Quociente =' +  Math.floor(x/y) + '' + '' + 'Resto = ' + x%y
    }
}

function Q2() {
    console.log('Q2');
    var cateto1 = Number.parseFloat(document.getElementById('cateto1').value);
    var cateto2 = Number.parseFloat(document.getElementById('cateto2').value);
    console.log ('Cateto 1:' + cateto1)
    console.log ('Cateto 2:' + cateto2)
    var res = (Math.sqrt (Math.pow (cateto1,2) + Math.pow (cateto2, 2)))
    console.log ('Hipotenusa:' + res)
    document.getElementById('RQ2').innerHTML = CalcularHipotenusa (cateto1, cateto2);
    function CalcularHipotenusa (cateto1, cateto2) {
        return  (Math.sqrt (Math.pow (cateto1,2) + Math.pow (cateto2, 2)))
    }
}
    

function Q3() {
    console.log('Q3');
    var aux = document.getElementById('profissoes');
    var profissao = aux.options[aux.selectedIndex].value ;
    document.getElementById ('RQ3').innerHTML = DeterminarGenero (profissao)
    function DeterminarGenero (profissao) {
    if (profissao == 'musicista' || profissao == 'presidente')
        return ('Ambos')
    else {
        if ( profissao.endsWith('a') || profissao.endsWith('iz'))
            return ('Feminino')
        if ( profissao.endsWith('o') || profissao.endsWith('or'))
            return ('Masculino')
    }
    }
}    














    function Q4() {
    console.log('Q4');
    var cateto3 = document.getElementById("cateto3").value;
    var cateto4 = document.getElementById("cateto4").value;
    var hipotenusa = document.getElementById("hipotenusa").value;
    document.getElementById('RQ4').innerHTML = CalculoLadoQualquerTrianguloRetangulo (cateto3, cateto4, hipotenusa)
    function CalculoLadoQualquerTrianguloRetangulo (cateto3, cateto4, hipotenusa) {
        if ( (hipotenusa) === '')
        {return (Math.sqrt ((Math.pow (cateto3,2) + Math.pow (cateto4,2))));}
        else if ( (cateto3) === '')
        {return (Math.sqrt (Math.pow (hipotenusa,2) - Math.pow (cateto4,2))); }
        else    if ( (cateto4) === '')
        {return (Math.sqrt (Math.pow (hipotenusa,2) - Math.pow (cateto3,2))); }
        else return 'Não coloque 3 elementos, apenas 2!'
    }
}

function Q5() {
    console.log('Q5');
    var altura = Number.parseFloat(document.getElementById('altura').value);
    var massa = Number.parseFloat(document.getElementById('massa').value);
    var aux = document.getElementById('generos');
    var genero = aux.options[aux.selectedIndex].value;
    imc =(massa/(altura*altura));
    document.getElementById ('RQ5').innerHTML = CalculoIMC (genero, imc)
    function CalculoIMC (genero, imc){
    if (genero == 'masculino1')
    {if (imc < 18.5 )
        {return('Magro')}
        else { if (imc >= 18.5 && imc < 24.9)
                {return ('Sarado')}
                else {if (imc >= 25 && imc < 29.9)
                    {return ('Rechonchudo')}
                    else {if (imc > 30)
                        {return ('Obeso')}}}}}
    else {{if (imc < 18.5 )
        {return ('Magra')}
        else { if (imc >= 18.5 && imc < 24.9)
                {return ('Sarada')}
                else {if (imc >= 25 && imc < 29.9)
                    {return ('Rechonchuda')}
                    else {if (imc > 30)
                        {return ('Obesa')}}}}}}
                    }
}
