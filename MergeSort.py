def sort(array):
    for p in range(0, len(array)):
        while p > 0:
            if array[p - 1] > array[p]:
                array[p], array[p - 1] = array[p - 1], array[p]
            p -= 1


array = [8, 3, 7, 0, 5, 4, 9, 2, 1, 6]
sort(array)
print(array)