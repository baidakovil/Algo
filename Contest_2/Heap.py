class Heap:
    def __init__(self):
        self.tree_ = list('0')
        self.size_ = len(self.tree_)-1

    def add_number(self, inp):
        self.size_ += 1
        self.tree_.insert(self.size_, int(inp))
        p = self.size_
        while p>1 and self.tree_[p // 2] < self.tree_[p]:
            self.tree_[p // 2], self.tree_[p] = self.tree_[p], self.tree_[p // 2]
            p = p // 2

    def extract(self):
        if self.size_ == 0:
            return 'CANNOT'
        else :
            value = self.tree_[1]
            self.tree_[1] = self.tree_[self.size_]
            self.size_ -= 1
            p_ex = 1
            while p_ex * 2 <= self.size_:
                if p_ex * 2 == self.size_: #только влево
                    max_idx = p_ex * 2
                elif self.tree_[p_ex*2] > self.tree_[p_ex*2+1]:
                    max_idx = p_ex*2
                else:
                    max_idx = p_ex * 2 + 1
                if self.tree_[p_ex] < self.tree_[max_idx]:
                    self.tree_[p_ex], self.tree_[max_idx] = self.tree_[max_idx], self.tree_[p_ex]
                p_ex = max_idx
            return value

    def clear(self):
        self.__init__()

a = Heap()

with open('input.txt') as f:
    for line in f:
        dodo = line.split()[0]
        if dodo == 'ADD':
            a.add_number(line.split()[1])
        elif dodo == 'EXTRACT':
            print(a.extract())
        elif dodo == 'CLEAR':
            a.clear()

# for line in open('input.txt').readlines():
#     dodo = line.split()[0]
#     if dodo == 'ADD':
#         a.add_number(line.split()[1])
#     elif dodo == 'EXTRACT':
#         print(a.extract())
#     elif dodo == 'CLEAR':
#         a.clear()