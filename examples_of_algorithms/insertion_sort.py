# Сортировка вставками
def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        ind = i - 1
        while ind >= 0 and array[ind] > item_to_insert:
            array[ind + 1] = array[ind]
            ind -= 1
        array[ind + 1] = item_to_insert


# Проверка
test_array = [5, 3, 1, 2, 0]
insertion_sort(test_array)
print(test_array)
# [0, 1, 2, 3, 5]
