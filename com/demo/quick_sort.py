def quick_sort(array):
    # 基线条件，如果数组为空或只有一个元素，即有序元素直接取值
    if len(array) < 2:
        return array
    # 递归条件
    else:
        # 使用第一个元素作为基准值
        pivot = array[0]
        # 由所有小于基准值的元素组成的数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的数组
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 4, 3, 2, 5]))
