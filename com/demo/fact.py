# 递归调用栈：阶乘
def fact(x):
    # 基线条件
    if x == 1:
        return 1
    # 递归条件
    else:
        return x * fact(x - 1)


# 栈顶在到达基线条件后的值为1，并从1开始对挂起的参数依次进行递归条件的运算操作
print(fact(5))
