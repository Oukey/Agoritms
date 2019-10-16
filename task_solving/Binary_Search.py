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
