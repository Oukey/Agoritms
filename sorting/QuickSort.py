# моделирование быстрой сортировки Хоара. Сложность O(N * log N)

def ArrayChunk(Array, left, right):
    '''
    Функция выполняет разбиение массива на две группы
    Принимает массив два индекса
    Возвращает индекс опорного элемента
    '''
    N = (left + right) // 2
    while left <= right:
        while Array[left] < Array[N]:
            left += 1
        while Array[right] > Array[N]:
            right -= 1
        if left <= right:
            Array[left], Array[right] = Array[right], Array[left]
            left += 1
            right -= 1
    return N


def QuickSort(array, left, right):
    '''
    Функция реализации быстрой сортировки Хоара
    Получает массив и два индекса
    '''
    if left >= right:
        return
    else:
        N = ArrayChunk(array, left, right)
        if N >= left + 1:
            QuickSort(array, left, N - 1)
        if N <= right - 1:
            QuickSort(array, N + 1, right)
