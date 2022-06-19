import timeit    
import time
import random

def sort(array):
    for final in range(len(array), 0, -1):
        for element in range(0, final, -1):
            if array[element] > array[element + 1]:
                array[element], array[element + 1] = array[element + 1], array[element]

inicio1 = timeit.default_timer()
x = 10
array1 = random.sample(range(10), x)
array1.sort(reverse=True)
fim1 = timeit.default_timer()

inicio2 = timeit.default_timer()
y = 50
array2 = random.sample(range(50), y)
array2.sort(reverse=True)
fim2 = timeit.default_timer()

inicio3 = timeit.default_timer()
z = 100
array3 = random.sample(range(100), z)
array3.sort(reverse=True)
fim3 = timeit.default_timer()

print(array1)
print(array2)
print(array3)
print('Tempo vetor 10 posições: %f' %  (fim1-inicio1))
print('Tempo vetor 50 posições: %f' %  (fim2-inicio2))
print('Tempo vetor 100 posições: %f' %  (fim3-inicio3))