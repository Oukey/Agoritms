# Реализация пирамидальной сортировки

def heap(array, heap_size, root_ind):
    largest = root_ind
    left_child = (2 * root_ind) + 1
    right_child = (2 * root_ind) + 2

    # Если левый потомок корня является допустимым индексом, элемент больше
    # чем текущий самый большой элемент, то обновляем самый большой элемент
    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child
    # Если самый большой элемент не является корневым, меняем их местами
    if largest != root_ind:
        array[root_ind], array[largest] = array[largest], array[root_ind]
        heap(array, heap_size, largest)


def heap_sort(array):
    # Создание кучи из списка array
    for i in range(len(array), -1, -1):
        heap(array, len(array), i)

    # перемещение корня в конец
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap(array, i, 0)


# Проверка работоспособности
array = [32, 12, 43, 8, 51]
heap_sort(array)
print(array)
# [8, 12, 32, 43, 51]
