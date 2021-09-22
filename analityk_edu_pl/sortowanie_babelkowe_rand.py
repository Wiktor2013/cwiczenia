import random
from random import randint
lista = [random.randint(0, 2501) for i in range(0, 101)]
print(lista)
def sortowanie_babelkowe(l):
    n = len(lista)
    while n > 1:
        zamiana = False
        for i in range(0, n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                zamiana = True
        n -= 1
        print(lista)
        if zamiana == False: break

    return lista
print(sortowanie_babelkowe(lista))
