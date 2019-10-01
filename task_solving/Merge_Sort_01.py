def MergeSort(array):
    '''
    Функция получает на вход исходный массив целых чисел
    Возвращает массив, отсортированный во убыванию
    '''
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left_list = MergeSort(array[:mid])
    right_list = MergeSort(array[mid:])
    return Merge(left_list, right_list)


def Merge(left_list, right_list):
    '''
    Функция слияния. Принимает два массива.
    Возвращает объединенный отсортированный массив
    '''
    sorted_list = []
    left_index = right_index = 0
    len_left_list, len_right_list = len(left_list), len(right_list)
    for _ in range(len_left_list + len_right_list):
        if left_index < len_left_list and right_index < len_right_list:
            # Проверка наименьшего значения в начале каждого списка
            # if left_list[left_index] <= right_list[right_index]:  # по возрастанию
            if left_list[left_index] >= right_list[right_index]:  # по убыванию
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1
        # Если достигли конца левого списка, добавляем элементы из правого списка
        elif left_index == len_left_list:
            sorted_list.append(right_list[right_index])
            right_index += 1
        # Если достигли конца правого списка, добавляем элементы из левого списка
        elif right_index == len_right_list:
            sorted_list.append(left_list[left_index])
            left_index += 1
    return sorted_list


# Проверка работоспособности
# array = [120, 45, 68.9, 250, -176]
# array = MergeSort(array)
# print(array)
# [-176, 45, 68.9, 120, 250]
