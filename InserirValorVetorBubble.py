import timeit    
import time
import random

def sort(array):
    for final in range(len(array), 0, -1):
        for element in range(0, final, -1):
            if array[element] > array[element + 1]:
                array[element], array[element + 1] = array[element + 1], array[element]

inicio1 = timeit.default_timer()
a = []
n = int(input('Tamanho do vetor: '))

for i in range(n):
    new_element = int(input('Indice: '))
    a.append(new_element)

a.sort()
fim1 = timeit.default_timer()

print(a)
print('Tempo ordenação vetor', n, 'posições: %f' %  (fim1-inicio1))