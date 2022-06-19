# O Insertion sort funciona da seguinte forma:
# Para cada posição no array é verificado se o item da esquerda é menor, 
# se for será feito a troca até que esse elemento pare na sua posição correta.

def sort(array):
    #For para pecorrer o array, onde p é a posição
    for p in range(0, len(array)):
        #Enquanto p for maior que 0 será verificado posição anterior
        while p > 0:
            # Se a posição atual menos anterior for maior que a posição atual, deve realizar a troca.
            if array[p - 1] > array[p]:
                # A troca será feita da seguinte maneira: Posição atual recebe posição anterior 
                # e a posição anterior recebe a posição atual.
                array[p], array[p - 1] = array[p - 1], array[p]
            # Decrementado a posição para evitar lup infinito.    
            p -= 1

array = [3, 6, 1, 1, 3, 3, 2, 0, 4, 3]
sort(array)
print(array)