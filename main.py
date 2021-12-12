'''
my sat tool kit
Author : 0764
--version 0.01 时间 2021/11/25
可以应用单子句规则了，重言式规则在一定程度上也可以使用，进行了一些基础性的工作
下次更新重点:1 添加子句sub_clause对象让clause对象可以更灵活的应对重言式规则，纯文字规则
           2 增加time模块的使用，将函数运行时间时间输出，可以尝试使用函数装饰器
一些idea 可以重构一个变元对象，里面存储一些相关的属性，这个可以在后面代码重构的时候可以尝试实现一下
'''
import copy

from func import  *
from obj import  *
import time
# 答案存为dict类型
solution = {}

def process(cla: clause):
    # print(f'processing -> {cla.cla}') # debug
    # 对于输入的句子无限循环
    while True:
        # print(f'processing in while ->  {cla.cla}')
        # 找到一个单子句中对应的变量
        var = find_unitary(cla)
        # print(f'var = {var}') # debug
        if var == None: # 如果找不到就跳出循环
            break
        else: # 否则就用单子句规则来处理这个句子
            solution[abs(var)] = var / abs(var)
            cla = unitary(cla,var)
        # print(f"cla.cla = {cla.cla}")
        if cla.cla == []: # 如果可以把一个句子处理成空的，那说明就是可满足的
            return True
        elif set() in cla.cla: # 如果出现了一个空的子句，说明就是不可满足的
            return False
    # ============跳出循环开始使用分裂规则==========
    # 寻找分裂的var
    add_key = select(cla)
    # deepcopy防止内存泄漏
    temp1 = copy.deepcopy(cla.cla)
    temp2 = copy.deepcopy(cla.cla)
    # 分别对于分裂出来的子句进行递归的运算
    temp1.append(({add_key}))
    if process(clause(temp1)):
        return True
    else:
        temp2.append(({-add_key}))
        return process(clause(temp2))


def tmain():
    # ------------------ input && initialize---------------------
    content = "请输入变元个数和子句个数，随后输入n行子句，子句以0结尾\nPS:变元数从1开始编号\n"
    var_num, cla_num = tuple(map(int,input(content).split()))
    clause_input = []
    for _ in range(cla_num):
        sub_cla_temp = list(map(int, input().split()))[:-1]
        clause_input.append(set(sub_cla_temp))
    print("your input clause is:",clause_input)
    my_cla = clause(clause_input)
    # ---------------------  processing --------------------------
    # while my_cla.cla_num == 0:
    #     pass
    start = time.perf_counter()
    keys = process(my_cla)
    end = time.perf_counter()
    print('Running time: %s Seconds' % (end - start))
    # 这里返回的keys 还要做
    # ----------------------- output -------------------------------
    if keys :
        print("SAT")
        print(f'solution = {solution}')
        # my_cla.show()
    else :
        print("UNSAT")

def main():
    import cProfile
    import pstats
    with cProfile.Profile() as pr:
        tmain()
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

if __name__ == '__main__':
    main()