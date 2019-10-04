class HeapSort:

    def __init__(self, array, depth=None):
    # def __init__(self):
        self.HeapObject = Heap()
        self.HeapObject.MakeHeap(array, depth)
        for el in array:
            self.HeapObject.Add(el)


    # def HeapSort(self, array, depth=None):
    # def HeapSort(self, array):
    #     # self.HeapObject.MakeHeap(array, depth)
    #     for el in array:
    #         self.HeapObject.Add(el)

    def GetNextMax(self):
        '''
        Метод возврата корня (максимального значения) с дальнейшей перестройкой кучи
        Возвращает значение корня или -1 если куча пуста
        '''
        # return self.HeapObject.GetMax()
        if not self.HeapObject.HeapArray:
            return - 1


class Heap:
    '''Класс кучи для реализации алгоритма HeapSort'''

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.HeapSize = 0

    def Get_size_depth(self, array):  # дополнительный метод
        '''
        Метод расчета и возврата глубины и размера кучи по размеру массива array
        Возвращает кортеж с параметрами: 0 - глубина кучи, 1 - размер кучи
        '''
        if array:
            depth_heap = 0
            size_heap = 0
            while size_heap < len(array):
                depth_heap += 1
                size_heap = 2 ** (depth_heap + 1) - 1
            return depth_heap, size_heap
        else:
            return 0, 0

    def MakeHeap(self, array, depth=None):  # основной вариант
        '''
        Метод создания массива кучи HeapArray из заданного массива 'a'
        Параметр 'depth' - глубина кучи
        '''
        if depth is None:
            self.HeapSize = self.Get_size_depth(array)[1]
        else:
            self.HeapSize = 2 ** (depth + 1) - 1
        for key in array:
            self.Add(key)

    def Add(self, key):
        '''
        Метод добавления нового элемента с ключем 'key' и перестройки кучи
        Возвращает True при добавлении или False если куча заполнена
        '''
        if len(self.HeapArray) < self.HeapSize:
            self.HeapArray.append(key)
            self.sift_up()
            return True
        else:
            return False

    def sift_up(self):
        '''Метод просеивание вверх'''
        ind = len(self.HeapArray) - 1
        while ind != 0:
            parent = (ind - 1) // 2
            if self.HeapArray[ind] <= self.HeapArray[parent]:
                break
            # if self.HeapArray[ind] > self.HeapArray[parent]:
            else:
                self.value_exchange(ind, parent)
                ind = parent

    def value_exchange(self, value_1, value_2):
        '''Метод обмена значениями двух элементов'''
        self.HeapArray[value_1], self.HeapArray[value_2] = self.HeapArray[value_2], self.HeapArray[value_1]

    def GetMax(self):
        '''
        Метод возврата корня (максимального значения) с дальнейшей перестройкой кучи
        Возвращает значение корня или -1 если куча пуста
        '''
        # if len(self.HeapArray) == 0:
        if not self.HeapArray:
            return - 1

        max_elem = self.HeapArray[0]
        if len(self.HeapArray) > 1:
            self.HeapArray[0] = self.HeapArray.pop(-1)
            self.sift_down()
        elif len(self.HeapArray) == 1:
            self.HeapArray = []
        return max_elem

    def sift_down(self):
        '''Метод просеивания вниз'''
        ind = 0
        end = len(self.HeapArray) - 1
        while True:
            child = 2 * ind + 1
            if child > end:
                break
            if child + 1 <= end and self.HeapArray[child] < self.HeapArray[child + 1]:
                child += 1
            if self.HeapArray[ind] < self.HeapArray[child]:
                self.value_exchange(ind, child)
                ind = child
            else:
                break


# Пример
# ar = [5, 4, 6, 7, 3, 8, 2, 9, 1, 10]
ar = [5, 4, 6, 7]


HS = HeapSort(ar)
# HS.HeapSort(ar)
# while i < len(ar):
#     print(HS.GetNextMax())
#     i += 1
for i in range(len(HS.HeapObject.HeapArray)):
    print(HS.GetNextMax())
print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())
# print(HS.GetNextMax())

print('0' * 60)
ss = Heap()
a = [3, 1, 2, 0]
ss.MakeHeap(ar)
for i in range(ss.HeapSize):
    print(ss.GetMax())
