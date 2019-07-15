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


def InsertionSortStep(array, step, i):
    '''
    Функция одного шага сортировки вставкой
    получает на вход массив целых чисел array,
    размер шага step (>=1) и номер элемента i (i>=0).
    Выполняется один цикл сортировки с шагом
    '''
    if step < 1 and i < 0:
        return array
    for i in range(i + step, len(array), step):
        item_to_insert = array[i]
        ind = i
        while ind >= step and array[ind - step] > item_to_insert:
            array[ind] = array[ind - step]
            ind -= step
        array[ind] = item_to_insert


def KnuthSequence(array_size):
    '''Функция вычисления интервальной последовательности целых чисел'''
    # Первый вариант
    ind_elem = 1
    list_step = [1]
    while 3 * ind_elem + 1 < array_size:
        ind_elem = 3 * ind_elem + 1
        list_step.insert(0, ind_elem)
    return list_step
    # Второй вариант - более затратный, зато в одну строчку =)
    # return [(lambda n: (3 ** n - 1) // 2)(n) for n in reversed(range(1, len_array)) if (3 ** n - 1) // 2 < len_array]
