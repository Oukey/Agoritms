# Алгоритмы сортировки - начало

def SelectionSortStep(array, i):
    '''
    Функция одного шага сортировки выбором.
    Получает массив array и новый элемент i (i >= 0)
    Меняет в этом массиве i-й элемент местами с минимальным элементом в оставшейся части массива,
    начиная с i+1
    '''
    if i < 0 or i > len(array):
        return array
    min_elem = i
    for elem in range(i + 1, len(array)):
        if array[min_elem] > array[elem]:
            min_elem = elem
    array[i], array[min_elem] = array[min_elem], array[i]

    # второй вариант
    # min_elem = array.index(min(array[i + 1::]))
    # if array[min_elem] < array[i]:
    #     array[i], array[min_elem] = array[min_elem], array[i]


def BubbleSortStep(array):
    '''
    Функция одного шага сортировки пузырьком.
    Получает массив целых чисел array
    и выполняет один пробег по массиву от начала к концу,
    меняя местами каждые два элемента i и i+1
    если i-й элемент больше i+1-го.
    Возвращает True, если по окончании пробега не было ни одного обмена элементов
    '''

    exchange = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            exchange = False
    return exchange
