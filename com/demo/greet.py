# 调用栈，用于存储多个函数的变量
def greet(name):
    # 按照函数顺序执行
    print('hello, ' + name + "!")
    # 调用greet2函数，此时greet处于挂起状态
    greet2(name)
    # 回到greet，打印输出
    print('getting ready to say bye...')
    # 调用bye函数，挂起greet
    bye()
    # 无函数调用，从函数返回


def greet2(name):
    print('how are you, ' + name + "?")


def bye():
    print('ok bye! ')


# 调用函数greet，在栈内存中分配空间
greet('jackson')
