# 创建字典，原理为散列表
voted = {}


# 使用散列表检查数据重复速度很快
def check_voter(name):
    if voted.get(name):
        print('kick them out')
    else:
        voted[name] = True
        print('let them vote')


check_voter('Tom')
check_voter('Mike')
check_voter('Mike')
