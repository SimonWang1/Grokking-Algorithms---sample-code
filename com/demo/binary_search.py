def binary_search(list, item):
    # 数组最大最小值下标
    low = 0
    high = len(list) - 1
    # 在数组范围内循环遍历
    while low <= high:
        # 数组中间值下标
        mid = (low + high)
        # 数组中间值
        guess = list[mid]
        # 找到数值并输出
        if guess == item:
            return mid
        # 若中间值比数值大，在小值范围内查找
        if guess > item:
            high = mid - 1
        # 若中间值比数值小，在大值范围内查找
        else:
            low = mid + 1
    # 若没找到返回空
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
