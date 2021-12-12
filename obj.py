class clause:
    var_cnt = {}
    solution = {}# not used

    def __init__(self,__cla):
        self.cla :list = __cla # list(set())
        self.cla_num :int =len(self.cla)
        self.load()

    def show(self):
        print(f'cla = {self.cla}\ncla_num = {self.cla_num}\nvar_num = {self.var_num}\n')
        print(f'var_cnt = {self.var_cnt}')

    # 将所有变元进行统计个数的处理，并且计算变元剩余个数
    def load(self):
        self.var_cnt = dict()
        for sub_cla in self.cla:
            for key in sub_cla:
                if key not in self.var_cnt:
                    self.var_cnt[key] = 1
                else:
                    self.var_cnt[key] += 1
        self.var_num = len(self.var_cnt.keys())
    # 重载 == 运算符
    def __eq__(self, other):
        if self.cla == other.cla:
            return True
        else:
            return False