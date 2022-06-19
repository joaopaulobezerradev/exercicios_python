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

