class Heap:
    def __init__(self):
        self.tree_ = list('0')
        self.size_ = len(self.tree_)-1

    def add_Point(self, point_inp): #замена названия функции и входящих данных
        self.size_ += 1
        self.tree_.insert(self.size_, point_inp)
        p = self.size_
        while p>1 and self.tree_[p // 2].magnitude > self.tree_[p].magnitude: #замена знака сравнения и значений на магнитуду
            self.tree_[p // 2], self.tree_[p] = self.tree_[p], self.tree_[p // 2]
            p = p // 2

    def extract(self):
        value = self.tree_[1] #замена значения на магнитуду
        self.tree_[1] = self.tree_[self.size_]
        self.size_ -= 1
        p_ex = 1
        while p_ex * 2 <= self.size_:
            if p_ex * 2 == self.size_:
                min_idx = p_ex * 2 #замена названия переменной
            elif self.tree_[p_ex*2].magnitude < self.tree_[p_ex*2+1].magnitude: #замена знака сравнения и значения на магнитуду
                min_idx = p_ex*2
            else:
                min_idx = p_ex * 2 + 1
            if self.tree_[p_ex].magnitude > self.tree_[min_idx].magnitude: #замена знака сравнения и значения на магнитуду
                self.tree_[p_ex], self.tree_[min_idx] = self.tree_[min_idx], self.tree_[p_ex]
            p_ex = min_idx
        return value.x, value.y

class Point:
    def __init__(self, x_inp, y_inp):
        self.x = x_inp
        self.y = y_inp
        self.magnitude = x_inp ** 2 + y_inp ** 2

file = open('input_PointSorting.txt')
n = int(next(file))

point_Heap = Heap()

for i in range(0, n):
    x,y = tuple(map(int, next(file).split()))
    point_Heap.add_Point(Point(x, y))

otvet = ''
for i in range(0, n):
    x, y = point_Heap.extract()
    otvet += f'{x} {y}\n'
print(otvet)