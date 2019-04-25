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
    var a_str = document.getElementById('a').value;
    var b_str = document.getElementById('b').value;
    var c_str = document.getElementById('c').value;
    if ( a == Number && b == Number)
        {console.log (Math.sqrt ((Math.pow (a,2) + Math.pow (b,2))))}
    if ( b == Number && c == Number)
        {console.log c = }
    
    
    

}