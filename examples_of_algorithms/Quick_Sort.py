'''Пример алгоритма быстрой сортировки QuickSort'''


def Partition(A, left, right):
    '''Функция разделения массива'''
    if left >= right:
        return right
    else:
        split = left
        pivot = A[right]
        for i in range(left, right + 1):
            if A[i] <= pivot:
                A[i], A[split] = A[split], A[i]
            split += 1
    return split - 1


def Quicksort(A, left, right):
    if right != left:
        split = Partition(A, left, right)
        if split >= left + 1:
            Quicksort(A, left, split - 1)
        if split <= right - 1:
            Quicksort(A, split + 1, right)


