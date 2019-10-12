class ksort:

    def __init__(self):
        self.items = [None] * 800

    def index(self, s):
        '''
        Метод вычисляет индекс строки s в массиве items,
        или возвращает -1, если строка неверного формата
        '''
        if self.validation_check(s) is True:
            return self.get_hash(s)
        return -1

    def add(self, s):
        '''
        Метод размещает строку s в массиве items в нужной позиции и возвращает True,
        а если строка некорректного формата, возвращает False
        '''
        if self.index(s) == - 1:
            return False
        self.items[self.index(s)] = s
        return True

    def get_hash(self, s):
        '''Дополнительный метод нахождения индекса для строки'''
        ind_s = ord(s[0]) - 97 + int(s[1]) * 10 + int(s[2])
        return ind_s

    def validation_check(self, s):
        '''Дополнительный метод проверки корректности строки'''
        if len(s) == 3:
            if ord(s[0]) in range(97, 104 + 1):
                if int(s[1:2]) in range(0, 99 + 1):
                    return True
        return False
