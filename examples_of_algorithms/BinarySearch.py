# Пример бинарного поиска
def BinarySearch(array, data):
    '''
    Функция принимает отсортированный массив и значение искомого элемента.
    Возвращает позицию найденного элемента или -1 если элемент отсутствует в массиве
    '''
    Left = 0
    Right = len(array) - 1
    while Left <= Right:
        mid = Left + (Right - Left) // 2
        if array[mid] > data:
            Right = mid - 1
        elif array[mid] < data:
            Left = mid + 1
        else:
            return mid
    return - 1
