'''
1. Расширить класс Heap
массив HeapArray должен хранить объекты класса HeapItem, состоящий из Key и Value
Метод Add расширить вторым параметром
Новый объект класса HeapItem создавать внутри метода Add
'''


class HeapItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит объекты класса HeapItem
        self.HeapSize = 0

    def Add(self, key, value):
        '''
        Метод добавления нового элемента с ключем 'key' и перестройки кучи
        Возвращает True при добавлении или False если куча заполнена
	    Доделать!!!
        '''
        HI = HeapItem(key, value)
        if len(self.HeapArray) < self.HeapSize:
            self.HeapArray.append(HI)
            self.sift_up()  # Проверить!!!
            return True
        else:
            return False

    def GetMax(self):
        '''
        Метод возврата корневого объекта класса HeapItem из массива HeapArray с дальнейшей перестройкой кучи
        Возвращает -1 если куча пуста
	    Доделать!!!
        '''
        if len(self.HeapArray) == 0:
            return - 1
        else:
            max_elem = self.HeapArray[0]
            if len(self.HeapArray) > 1:
                self.HeapArray[0] = self.HeapArray.pop(-1)
                self.sift_down()  # !!! дополнительный метод. Проверить!!!
            elif len(self.HeapArray) == 1:
                self.HeapArray = []
            return max_elem

    def Len(self, array):
        '''Метод возврата количества элементов в куче'''
        return len(self.HeapArray)
        # или
        # return self.Get_size_depth(arrey)[1]

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

    def MakeHeap(self, array, depth=None):
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

    def sift_up(self):
        '''Метод просеивание вверх'''
        # Проверить!!!
        ind = len(self.HeapArray) - 1
        while ind != 0:
            parent = (ind - 1) // 2
            if self.HeapArray[ind.value] <= self.HeapArray[parent.value]:
                break
            # if self.HeapArray[ind.value] > self.HeapArray[parent.value]:
            else:
                self.value_exchange(ind, parent)
                ind = parent

    def sift_down(self):
        '''Метод просеивания вниз'''
        ind = 0
        end = len(self.HeapArray) - 1
        while True:
            child = 2 * ind + 1
            if child > end:
                break
            if child + 1 <= end and self.HeapArray[child.value] < self.HeapArray[child.value + 1]:
                child += 1
            if self.HeapArray[ind.value] < self.HeapArray[child.value]:
                self.value_exchange(ind, child)
                ind = child
            else:
                break

    def value_exchange(self, ind, parent):
        # Проверить!!!
        '''Метод обмена значениями двух элементов'''
        self.HeapArray[ind.value], self.HeapArray[parent.value] = self.HeapArray[parent.value], self.HeapArray[
            ind.value]
