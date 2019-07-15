dic = {
    "I" : "Eu"
}
#Funções
def imprime(x):
    """
    X: da um print da funcao
    """                        #--->String MultiLinha, usada para se tornaro "HELP"  da funcao
    print(x)

imprime(2)
imprime('Oi Mundo!')
imprime(dic)
imprime((1, 2, 3))
imprime(None)
imprime([True, False])

def distancia(a, b):
    """
    A, B são listas, Tuplas, ETC. Tem que ter pelo menos dois elementos
    Retorna a distancia EUclidiana de a, b
    """
    return ((a[0] - b[0]**2 - (a[1] - b[1]**2)))**0.5

imprime(distancia)
imprime(distancia( (0,0), (3,4) ))
imprime(distancia( [0,0], [3,4] )) 
imprime(distancia( (0,0), [3,4,4,5,6,3,4,5,6,1,2,3,1,2,] ))

def divisaoInteira(x, y):
    """
    X, Y sao numeros
    Retorna o quociente e resto 
    """
    return (x//y, x%y)

quociente, resto = divisaoInteira(15, 8)
print('Quociente:', quociente, '     Resto: ', resto)


def mapear(funcao, lista):
    return list(funcao(elemento) for elemento in lista)

def quadrado(x):
    return x**2

def raizQuadrada(x):
    return x**0.5

lista = list(i for i in range(11))
print(lista)
print(mapear(quadrado, lista))
print(mapear(raizQuadrada, lista))
