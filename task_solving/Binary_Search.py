# Алгоритм двоичного поиска
class BinarySearch:

    def __init__(self, array):
        self.array = array
        self.Left = 0
        self.Right = len(array) - 1
        self.result = 0  # 0 - поиск, +1 - элемент найден; -1 элемент не найден

    def Step(self, N):
        '''Метод выполнения одного шага поиска. Прнимает искомое число (int)'''
        step = (self.Left + self.Right + 1) // 2
        if N == self.array[step]:  # Если элемент найден
            self.result = 1
            # self.Left, self.Right = step
        if N > self.array[step]:  # Если элемент больше среднего в диапазоне
            # self.Left = step
            self.Left = step - 1
        if N < self.array[step]:  # Если элемент меньше среднего в диапазоне
            # self.Right = step
            self.Right = step + 1
        if self.Left == self.Right:  # Если элемент не найден
            self.result = -1

    def GetResult(self):
        return self.result


array = [num for num in range(0, 11)]
print(array)
N = 8
BS = BinarySearch(array)

while BS.result == 0:
    BS.Step(N)
# BS.Step(N)
print('Левый предел: ', BS.Left)
print('Правый предел: ', BS.Right)
print('Результат:', BS.result)
# BS.Step(N)
# print('Левый предел: ', BS.Left)
# print('Правый предел: ', BS.Right)
# print('Результат:', BS.result)
# BS.Step(N)
# print('Левый предел: ', BS.Left)
# print('Правый предел: ', BS.Right)
# print('Результат:', BS.result)
# BS.Step(N)
# print('Левый предел: ', BS.Left)
# print('Правый предел: ', BS.Right)
# print('Результат:', BS.result)
# BS.Step(N)
# print('Левый предел: ', BS.Left)
# print('Правый предел: ', BS.Right)
# print('Результат:', BS.result)
# BS.Step(N)
# print('Левый предел: ', BS.Left)
# print('Правый предел: ', BS.Right)
# print('Результат:', BS.result)
# BS.Step(N)
# print('Левый предел: ', BS.Left)
# print('Правый предел: ', BS.Right)
# print('Результат:', BS.result)
# BS.Step(N)
# print('Левый предел: ', BS.Left)
# print('Правый предел: ', BS.Right)
# print('Результат:', BS.result)
#
#
#
#
#
print(int((0 + 1)//2))
