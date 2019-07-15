import math 
import random as rnd 
from os import path
from hashlib import sha256
import continuacao2 as Minhabiblioteca

alpha = list((a/10)*2*math.pi for a in range(11))
print(alpha)
print(list(map(math.cos, alpha)))


#Dado
def dado():
    """
    Simula um dado de 20 lados
    """
    return rnd.randint(1, 20)

for i in range(10): ##---> Joga o dado 10 vezes
    print(dado())

#Criptografia 
print(sha256(b'Felipe Narimatsu Presti').hexdigest())
print(sha256(b'Igor Peretta').hexdigest())

print(Minhabiblioteca.divisaoInteira(10, 5)) #---> Usando a biblioteca "Minhabiblioteca" definida no topo da pagina e utilizando suas funcoes