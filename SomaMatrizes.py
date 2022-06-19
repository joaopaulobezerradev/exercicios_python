import timeit
from random import randint

tamanhoVetor = int(input('Tamanho do vetor: '))

listaA = [0]*tamanhoVetor
listaB = [0]*tamanhoVetor
listaR = [0]*tamanhoVetor

for i in range (len(listaA)):
    listaA[i] = i*2


for i in range (len(listaB)):
    listaB[i] = i*3

inicio = timeit.default_timer()
for i in range (len(listaR)):
    listaR[i] = listaA[i]*listaB[i]

fim = timeit.default_timer()

print(listaA)
print(listaB)

print(listaR)
print('%f' % (fim-inicio))

def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %matriz[i][j])
            else:
                print("%d" %matriz[i][j], end = " ")
    print()

n = int(input('Número de linhas da matriz: '))
m = int(input('Número de colunas da matriz: '))

matriz = []

inicio = timeit.default_timer()
for i in range(n):
        linha = []
        for j in range(m):
            linha.append(randint(1,100))
            matriz.append(linha)

fim = timeit.default_timer()

imprime_matriz(matriz)
print('%f' % (fim-inicio))







