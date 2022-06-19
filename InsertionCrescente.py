import timeit    
import time
import random

def sort(array):
    for i in range(0, len(array)):
        while i > 0:
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

inicio1 = timeit.default_timer()
x = 10
array1 = random.sample(range(10), x)
sort(array1)
fim1 = timeit.default_timer()

inicio2 = timeit.default_timer()
y = 50
array2 = random.sample(range(50), y)
sort(array2)
fim2 = timeit.default_timer()

inicio3 = timeit.default_timer()
z = 100
array3 = random.sample(range(100), z)
sort(array3)
fim3 = timeit.default_timer()


print(array1)
#print(array2)
#print(array3)
print('Tempo vetor 10 posições: %f' %  (fim1-inicio1))
print('Tempo vetor 50 posições: %f' %  (fim2-inicio2))
print('Tempo vetor 100 posições: %f' %  (fim3-inicio3))