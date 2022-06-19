import timeit    
import time
import random

def sort(array):
    for i in range(len(array)):
        while i > 0:
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

inicio1 = timeit.default_timer()
x = int(input('Digite o tamanho do vetor: '))
array = random.sample(range(50), x)
array.sort(reverse=True)
fim1 = timeit.default_timer()

print(array)
print('Tempo vetor', x, 'posições: %f' %  (fim1-inicio1))


