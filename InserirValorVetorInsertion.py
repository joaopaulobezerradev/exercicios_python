import timeit    
import time
import random

def insertion(array):
    for i in range(0, len(array)):
        while i > 0:
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

inicio1 = timeit.default_timer()
a = []
n = int(input('Tamanho do vetor: '))

for i in range(n):
    new_element = int(input('Indice: '))
    a.append(new_element)

insertion(a)
fim1 = timeit.default_timer()

print(a)
print('Tempo vetor', n, 'posições: %f' %  (fim1-inicio1))