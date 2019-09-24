# пример сортировки выбором
def selection_sort(array):
    for i in range(len(array)):
        if i < 0 or i > len(array):
            return array
        min_elem = i
        for elem in range(i + 1, len(array)):
            if array[elem] < array[min_elem]:
                min_elem = elem
        array[i], array[min_elem] = array[min_elem], array[i]


# Проверка
test_array = [5, 3, 1, 2, 0]
selection_sort(test_array)
print(test_array)
# [0, 1, 2, 3, 5]