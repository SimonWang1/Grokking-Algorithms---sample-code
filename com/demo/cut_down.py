# 简单递归
def cut_down(i):
    print(i)
    # 基线条件
    if i <= 0:
        return
    # 递归条件
    else:
        cut_down(i - 1)


cut_down(3)
