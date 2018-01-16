# 选择排序
def find_smallest(arr):
    # 存储最小索引和元素的值
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 对数组排序
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # 找到最小的元素，并添加到新数组中
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 9, 10, 2]))
