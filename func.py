import copy

from obj import *

def find_unitary(cla:clause):
    # 寻找单子句
    for sub_cla in cla.cla:
        if len(sub_cla) == 1:
            return sub_cla.pop()
        # temp = sub_cla.pop()
        # if sub_cla == set():
        #     return temp
        # else:
        #     sub_cla.add(temp)
    return None

def unitary(cla : clause, var ):
    # 使用列表生成式 过滤掉空的set
    cla.cla = [s for s in cla.cla if len(s) != 0]
    # cla.cla = [s for s in cla.cla if s!=set()]
    # cla.cla_num = len(cla.cla)
    # 使用deepcopy防止内存泄漏
    temp_cla = copy.deepcopy(cla.cla)
    for sub_cla in temp_cla:
        if var in sub_cla:
            sub_cla.clear()
    temp_cla = [s for s in temp_cla if s!=set()]
    # temp_cla = [s for s in temp_cla if len(s)!=0]
    # 判断cla.cla的两种可能情况
    if temp_cla == []:
        cla.cla = []
    else:
        cla.cla = temp_cla
        for sub_cla in cla.cla:
            if -var in sub_cla:
                sub_cla.remove(-var)
    return cla

def select(cla : clause):
    # 选取句子中出现次数最多的变量
    cla.load()
    select_dict = {}
    max_cnt = -1
    max_key = None
    # 遍历var_cnt，存储相应的变元出现次数
    for key in cla.var_cnt.keys():
        if abs(key) in select_dict:
            select_dict[abs(key)] += cla.var_cnt[key]
        else:
            select_dict[abs(key)] = cla.var_cnt[key]
    # 选取出现次数最多的var
    for key in select_dict.keys():
        if max_cnt < select_dict[key]:
            max_key = key
    # print(f'max_key = {max_key}') # debug
    return max_key

def plain_text(cla: clause):
    # 纯文字规则的一种实现但是没有用到，应当改进后续算法使用这一规则
    plain_text_list = []
    keys = set(cla.var_cnt.keys()).copy()

    for key in keys:
        if -key not in keys:
            plain_text_list.append(key)

    for text in plain_text_list:
        cla.solution[abs(text)] = text / abs(text)
        cla.var_num -= 1
        print(f'text = {text}')
        for sub_cla in cla.cla:
            if text in sub_cla:
                sub_cla.remove(text)
    # cla.cla = [s for s in cla.cla if s!=set()]
    cla.cla = [s for s in cla.cla if len(s)!=0]
    cla.cla_num = len(cla.cla)
    cla.load()
    return cla

def tautology(cla : clause):
    # 矛盾式规则也没用到。
    for sub_cla in cla.cla:
        for var in sub_cla:
            if -var in sub_cla:
                cla.cla.remove(sub_cla)
                cla.cla_num -= 1
                break
    return cla
