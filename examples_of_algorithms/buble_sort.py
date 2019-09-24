# Пример пузырьковой сортировки
def bubble_sort(nums):
    swapped = True  # флаг для прерывания цикла while
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


# Проверка
test_array = [5, 3, 1, 2, 0]
bubble_sort(test_array)
print(test_array)
# [0, 1, 2, 3, 5]
