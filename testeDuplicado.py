import random
import timeit    
import time

def somarMatrizes(matriz1, matriz2):

    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
    return result

def produtoMatrizes(matriz11, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] * matriz2[i][j])
    return result

def imprimirMatriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %matriz[i][j])
            else:
                print("%d" %matriz[i][j], end = " ")
    print()

matriz1 = []
n = int(input("Número linhas da matriz 1: "))
m = int(input("Número colunas da matriz 1: "))

inicio = timeit.default_timer()
for i in range(n):
     matriz1.append([])
     for j in range(m):
        matriz1[i].append(random.randint(0,100))

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print(matriz1[i][j], end=" ")
    print ("\n")
fim = timeit.default_timer()

matriz2 = []
n = int(input("Número linhas da matriz 2: "))
m = int(input("Número colunas da matriz 2: "))

inicio = timeit.default_timer()
for i in range(n):
     matriz2.append([])
     for j in range(m):
        matriz2[i].append(random.randint(0,100))

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print(matriz2[i][j], end=" ")
    print ("\n")
fim = timeit.default_timer()

imprimirMatriz
print('Soma das Matrizes:', somarMatrizes(matriz1, matriz2))
print('Produto das Matrizes:', produtoMatrizes(matriz1, matriz2))

print('Tempo: %f' %  (fim-inicio))



