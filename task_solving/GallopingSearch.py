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
    while ind_calc(i) < len(array) - 1:
        ind = int(ind_calc(i))
        if array[ind] == data:
            return True
        if array[ind] < data:
            i += 1
        else:
            break
    # Если элемент массива с расчетным индексом больше искомого значения data
    BS = BinarySearch(array)
    if ind_calc(i) >= len(array):
        BS.Right = len(array) - 1
    else:
        BS.Right = int(ind_calc(i))
    while BS.GetResult() == 0:
        BS.Step(data)
    if BS.GetResult() == 1:
        return True
    else:
        return False


def ind_calc(i):
    '''Функция расчета повышения индекса'''
    return 2 ** (i - 2)
