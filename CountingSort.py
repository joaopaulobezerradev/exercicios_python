import timeit    
import time

def jls_extract_def():
    return 1


def countingSort(array):

    tamanho = len(array)

    resultado = [0] * tamanho


    count = [0] * 10


    for i in range(0, tamanho):

        count[array[i]] += jls_extract_def()


    for i in range(1, 10):

        count[i] += count[i - 1]


    i = tamanho - 1

    while i >= 0:

        resultado[count[array[i]] - 1] = array[i]

        count[array[i]] -= 1

        i -= 1


    for i in range(0, tamanho):

        array[i] = resultado[i]


inicio1 = timeit.default_timer()
a = []

n = int(input('Tamanho do vetor: '))


for i in range(n):

    new_element = int(input('Indice: '))

    a.append(new_element)


countingSort(a)

fim1 = timeit.default_timer()

print(a)

print('Tempo ordenação counting sort no vetor', n, 'posições: %f' %  (fim1-inicio1))





