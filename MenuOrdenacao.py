from time import sleep
import timeit    
import time
import random

def insertion(array):
    for i in range(0, len(array)):
        while i > 0:
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

def sort(array):
    for final in range(len(array), 0, -1):
        for element in range(0, final, -1):
            if array[element] > array[element + 1]:
                array[element], array[element + 1] = array[element + 1], array[element]

def countingSort(array):
    tamanho = len(array)
    resultado = [0] * tamanho

    count = [0] * 10

    for i in range(0, tamanho):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = tamanho - 1
    while i >= 0:
        resultado[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, tamanho):
        array[i] = resultado[i]

def buscaSequencial(list, item):
    p = 0
    encontrado = False

    while p < len(list) and not encontrado:
        if list[p] == item:
            encontrado = True
        else:
            p = p+1
    return encontrado

print('*** Ordenação Algoritimos ***\n')
opcao = 0
while opcao != 5:
    print('''
    [1] Insertion sort
    [2] Bubble sort
    [3] Counting sort
    [4] Busca sequencial
    [5] Sair\n''')
    opcao = int(input('Escolha umas das opções: '))
    if opcao == 1:
        inicio1 = timeit.default_timer()
        a = []
        n = int(input('Tamanho do vetor: '))

        for i in range(n):
            new_element = int(input('Valor: '))
            a.append(new_element)

        insertion(a)
        fim1 = timeit.default_timer()

        print(a)
        print('Tempo ordenação insertion sort no vetor', n, 'posições: %f' %  (fim1-inicio1))
        
    
    elif opcao == 2:
        inicio1 = timeit.default_timer()
        a = []
        n = int(input('Tamanho do vetor: '))

        for i in range(n):
            new_element = int(input('Valor: '))
            a.append(new_element)

        a.sort()
        fim1 = timeit.default_timer()

        print(a)
        print('Tempo ordenação bubble sort no vetor', n, 'posições: %f' %  (fim1-inicio1))
        

    elif opcao == 3:
       inicio1 = timeit.default_timer()
       a = []
       n = int(input('Tamanho do vetor: '))

       for i in range(n):
            new_element = int(input('Valor: '))
            a.append(new_element)

       countingSort(a)
       fim1 = timeit.default_timer()

       print(a)
       print('Tempo ordenação counting sort no vetor', n, 'posições: %f' %  (fim1-inicio1))

    elif opcao == 4:
        lista = []
        n = int(input('Numero indices da lista: '))

        for i in range(n):
            new_element = int(input('Valor: '))
            lista.append(new_element)

        b = int(input('Item a ser busca na lista: '))

        inicio = timeit.default_timer()
        print('Item na lista => ', buscaSequencial(lista, b))
        fim = timeit.default_timer()

        print(lista)
        print('Tempo da busca do item na lista: %f' % (fim - inicio))

    elif opcao == 5:
        print('Finalizando programa....')

    else:
        print('Opção Inválida')
    sleep(2)

print('Programa encerrado!!!')