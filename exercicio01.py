git import timeit
import time

def buscaSequencial(list, item):
    p = 0
    encontrado = False

    while p < len(list) and not encontrado:
        if list[p] == item:
            encontrado = True
        else:
            p = p+1
    return encontrado

lista = []
n = int(input('Numero indices da lista: '))

for i in range(n):
    new_element = int(input('Valor '))
    lista.append(new_element)

b = int(input('Item a ser busca na lista: '))

inicio = timeit.default_timer()
print('Item na lista => ', buscaSequencial(lista, b))
fim = timeit.default_timer()

print(lista)
print('Tempo da busca do item na lista: %f' % (fim - inicio))


    