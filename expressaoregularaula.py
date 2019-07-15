import re

#Dectectar telefones normais ou celulares

telefone = re.compile(r'\(\d{2,3}\)\s*\d{4,5}-\d{4}')

textoparaserprocurado = """Meus telefones são (16)98126-8810 ou (016)     3636-1818
"""

info = telefone.findall(textoparaserprocurado)



for i in info:
    print(''.join(i))

# Detectar siglas, endereçõs de internet e ...

siglas = re.compile(r'[A-Z]{2,}')
urls = re.compile(r'(([w]{3}\.){0,1}([a-zA-Z][a-zA-Z0-9]{0,}\.){1,}([a-zA-Z]{2,4}))')

texto = """Os endereços da Internet são mais conhecidos pelos nomes associados aos 
endereços IP (por exemplo, o nome www.wikipedia.org está associado ao IP 208.80.152.130[4]).
 Para que isto seja possível, é necessário traduzir (resolver, em inglês, ou resolvedor) 
 os nomes em endereços IP. O Domain Name System (DNS) é um mecanismo que converte nomes em 
 endereços IP e vice-versa. Assim como o endereçamento CIDR, os nomes DNS são hierárquicos 
 e permitem que faixas de espaços de nomes sejam delegados a outros DNS. Acessado a partir de feelt.ufu.br
 e Goole.com.br.
 """

info = siglas.findall(texto)

for i in info:
     print(i)

info = urls.findall(texto)

for i in info:
    print(i[0])
