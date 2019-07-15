#Tipos Básicos
a = 1                                  #inteiros
b = 1.7                                #ponto flutuante
c = 'c'                                #string
d = 'VOU GABARITAR A P3 DE CÁLCULO!!!' #string
e = d[2]
print(a, b, c, d, e)

#Operadores aritméticos: + - / // % **
x = 3 + 5
y = 7 - 1
z = 5/2                                #--> Divisão (considerando número flutuante)
w = 5//2                               #--> Divisão inteira
u = 5%2                                #--> Resto
v = 5**2                               #--> Elevado
t = 25**(1/2)                          #--> Raiz elevado a 0.5
print(x, y, z, w ,u ,v, t)

#Conversão entre tipos
r = int(2.9)
s = float(3)
f = str(r) 
g = float('23.9') + 1
print(r, s, f, g)


#String
msg = 'The quick brown fox jumps over the lazy dog'
print(len(msg))                       #--> Retorna o tamanho da string
s0 = msg[4:9]                         #--> Corta a string nas posições X e Y
print(s0)
s1 = msg[40:]
print('1:',s1)
s2 = msg[:3]
print('2:',s2)
s3 = msg[-8:]
print('3:', s3)
s4 = msg[-8:-4]
print('4:', s4)
s5 = msg[-1]
print('5:', s5)
s6 = msg.upper()
print('6:', s6)
s7 = msg.lower()
print('7:', s7)
s8 = 'felipe narimatsu'.upper()
print('8:', s8)
s9 = 'felipe narimatsu'[7:16] 
print('9:', s9)
msg1 = '\n      meu texto          \t\t' 
print(msg1)
msg2 = '\t\t 3;4;5;6;-7;felipe;xx\n'.strip()     #--> strip() {retira coisas desnecessárias da string}
print(msg2.split(';'))

#Caracteres de escape: \?, onde ? é um 'comando'
# \n  : nova linha
# \t  : nova linha
# \\  : tab (identação)
# \'  : '
# \"  : "
caracteres = "\n\t'\\\""
print(caracteres)

#Lógica Booleana
q0 = True
q1 = False
q2 = q0 and q1
q3 = q0 or q1
q4 = not q3

#Decisão 
if q4 and not q3:
    print('Olá')
elif q1 and not q2:
    print('Anime é bom!')
else:
    print('Adeus!')


#Comparações 
print(3 > 4)
print(3 >= 4)
print(3 < 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4, not(3 == 4))



#Arrays / Listas
li = [1,2,3,4,5]
print(li)
li2 = [1,'2',3.5, "Felipe".upper()]
print(li2)
#Referencia da lista igual a da string
print(li[:3])
#Metedo append insere elementos na lista
li.append('novo elemento')
print(li)
#Operador + concatena listas
print(list(range()1,4)) + ['***'] + [5,6,7])




#Laço(FOR)
stri = ''
for i in range(5):
    stri += str(i) + ' '
print(stri)

