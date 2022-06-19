from time import sleep
import timeit    
import time
import random

def sort(array):
    for p in range(0, len(array)):
        while p > 0:
            if array[p - 1] > array[p]:
                array[p], array[p - 1] = array[p - 1], array[p]
            p -= 1

print('*** Ordenação Algoritimos ***\n')
opcao = 0
while opcao != 3:
    print('''
    [1] Merge sort
    [2] Quick sort
    [3] Sair\n''')
    opcao = int(input('Escolha umas das opções: '))
    if opcao == 1:
        inicio1 = timeit.default_timer()
        a = []
        n = int(input('Tamanho do vetor: '))

        for i in range(n):
            new_element = int(input('Valor: '))
            a.append(new_element)

        sort(a)
        fim1 = timeit.default_timer()

        print(a)
        print('Tempo ordenação merge sort no vetor', n, 'posições: %f' %  (fim1-inicio1))
        
    
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
        print('Tempo ordenação quick sort no vetor', n, 'posições: %f' %  (fim1-inicio1))
      
    elif opcao == 3:
        print('Finalizando programa....')

    else:
        print('Opção Inválida')
    sleep(2)

print('Programa encerrado!!!')