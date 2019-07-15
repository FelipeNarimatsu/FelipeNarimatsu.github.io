#Tipos de dados 
a = None 
#Verificar se a variável é None: 
if a is None:
    print("a não é nada")

b = list(i for i in range(5))
b = None
if not (b is None):
    print(b)

lista = [1, 2, 3, 4, 5]
tupla = tuple() #tupla vazia ---> tupla é uma lista que não pode ter seus elementos alterados
tupla = [2, 3, 4, 5, 6]
print(lista, tupla)

#Dicionário
dic = dict() #dicionário vazio
dic1 = {
    'zero' : 0,
    'um' : 1,
    'dois' : 2,
    'tres' : 3,
}
print(dic['um'])

#Código feito pelo PEretta
msg = 'Custa tres reais'
novamsg = []
for palavra in msg.split(): #---> corta a string onde tem espaços
    if palavra in dic.keys(): #---> verifica se a parte cortada da string pertence aos elementos dentro da chave do dic acima
        nova.append(str(dic[palavra])
   else:
        novamsg.append(palavra)
novamsg = ' '.join(novamsg)
print(novamsg)


dic = {
    "I" : "Eu"
    "like" : "Gosto"
    "anime" : "de anime"
    "!" : "!"
}
msg = "I like anime !"
traducao = []
for palavra in msg.split():
    if palavra in dic.keys():
        traducao.append(dic[palavra])
    else:
        traducao.append(palavra)
print(' '.join(traducao))

