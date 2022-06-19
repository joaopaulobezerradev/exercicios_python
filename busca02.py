lista =[10, 5, 15, 12, 35, 25, 1, 82, 98]

def buscaBinaria(lista, chave):
    inicio=0
    fim=len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

print(buscaBinaria(lista, 35))
print(buscaBinaria(lista, 10))


