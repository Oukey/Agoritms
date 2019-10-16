# Алгоритм двоичного поиска
class BinarySearch:

    def __init__(self, array):
        self.array = array
        self.Left = 0
        self.Right = len(array) - 1
        self.result = 0  # 0 - поиск, +1 - элемент найден; -1 элемент не найден

    def Step(self, N):
        '''Метод выполнения одного шага поиска. Прнимает искомое число (int)'''
        if self.array[self.Left] > N or self.array[self.Right] < N:
            self.result = -1
        mid = self.Left + (self.Right - self.Left) // 2
        if self.result == 0:
            if self.array[mid] == N:
                self.result = 1
            else:
                if self.Left == self.Right:
                    self.result = -1
                else:
                    if self.array[mid] > N:
                        self.Right = mid - 1
                    elif self.array[mid] < N:
                        self.Left = mid + 1

    def GetResult(self):
        return self.result


def GallopingSearch(array, data):
    '''
    Функция бинарного поиска "от края"(экспоненциальный поиск)
    Принимает отсортированный массив и искомое целое значение
    Возвращает True если число найдено и False в обратном случае
    '''
    array = sorted(array)
    i = 1
    ind = 2 ** (i - 2)
    if array[ind] == data:
        return True
    elif array[ind] < data:
        i = 2
        if ind < len(array) - 1:
            if array[ind] == data:
                return True
            else:
                ind = len(array) - 1


