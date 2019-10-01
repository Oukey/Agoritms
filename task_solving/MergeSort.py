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

    # def Len(self, array):
    def Len(self):
        '''Метод возврата количества элементов в куче'''
        # return len(self.HeapArray)
        # или
        return self.HeapSize
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


class MergeSort:

    def __init__(self, array):
        self.MergeArray = array
        self.MergeHeap = Heap
        self.CurrentItem = HeapItem
        self.mid = len(self.MergeArray) // 2

    def Merge(self):
        # mid = len(self.MergeArray) // 2
        # сортировка и объединение каждой половины
        first_list = sorted(self.MergeArray[:self.mid], reverse=True)
        second_list = sorted(self.MergeArray[self.mid:], reverse=True)
        self.MergeArray = first_list + second_list

    def MergeSortStep(self):
        f_ind = 0
        s_ind = self.mid
        len_array = len(self.MergeArray)
        if f_ind < self.mid and s_ind < len_array:
            self.MergeHeap.Add(1, self.MergeArray[f_ind])
            self.MergeHeap.Add(2, self.MergeArray[s_ind])
            f_ind += 1
            s_ind += 1

        elif s_ind == len_array and f_ind < self.mid:
            self.CurrentItem = HeapItem(1, self.MergeArray[f_ind])
            f_ind += 1

        elif s_ind < len_array and f_ind == self.mid:
            self.CurrentItem = HeapItem(1, self.MergeArray[s_ind])
            s_ind += 1

        if s_ind < len(self.MergeArray):
            self.MergeHeap.Add(self.MergeArray[s_ind], 2)

        if self.MergeHeap.Len() > 0:
            self.CurrentItem = self.MergeHeap.GetMax()
        else:
            self.CurrentItem = None

    def merge(self, left_list, right_list):
        ''' Метод слияния. Принимает массив/список. Возвращает два массива/списка '''
        sorted_list = []
        left_ind = right_ind = 0
        len_left_list, len_right_list = len(left_list), len(right_list)
        for _ in range(len_left_list + len_right_list):
            if left_ind < len_left_list and right_ind < len_right_list:
                # Проверка наименьшего значения в начале каждого списка
                if left_list[left_ind] >= right_list[right_ind]:  # по убыванию, если <= будет по возрастанию
                    sorted_list.append(left_list[left_ind])
                    left_ind += 1
                else:
                    sorted_list.append(right_list[right_ind])
                    right_ind += 1
            # Если достигли конца левого списка, добавляем элементы из правого списка
            elif left_ind == len_left_list:
                sorted_list.append(right_list[right_ind])
                right_ind += 1
            # Если достигли конца правого списка, добавляем элементы из левого списка
            elif right_ind == len_right_list:
                sorted_list.append(left_list[left_ind])
                left_ind += 1
            # Если закончились оба списка, добавляем None
            elif left_ind == len_left_list and right_ind == len_right_list:
                sorted_list.append(None)
        return sorted_list

    def merge_sort(self, array):
        ''' Метод сортировки слиянием. Принимает массив/список. Возвращает два массива/списка '''
        # Если состоит из одного элумента, возвращаем его
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        # сортировка и объединение каждой половины
        left_list = self.merge_sort(array[:mid])
        right_list = self.merge_sort(array[mid:])
        # Объединение отсортированных списков в новый
        return self.merge(left_list, right_list)


# ПРоверка работоспособности
ar = [4, 3, 5, 2, 6, 1, 7]
sorting = MergeSort(ar)
ar = sorting.merge_sort(ar)
print(ar)
