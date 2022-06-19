import timeit
import time
import random

def buscas (lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            print(i)
            return i
    return -1

lista = [2, 3, 5, 6, 5, 8, 0, 7, 9]
chave = [5]
v = 10

for i in range(len(lista)):
    lista = random.sample(range(50), v)
    buscas(lista, chave)

inicio = timeit.default_timer()
print(buscas(lista, chave))
fim = timeit.default_timer()
    
#print(' %f' % (fim - inicio))
print('Tempo vetor 10 posições: %f' %  (fim-inicio))
