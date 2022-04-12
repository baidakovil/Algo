# import math
#
# class Heap:
#     def __init__(self, n):
#         self.tree_ = [(math.inf,j) for j in range(0,n+1)]
#         self.tree_[0] = 0
#         self.tree_[1] = (0,1)
#         self.size_ = len(self.tree_)-1
#         self.pointers = [k for k in range(0,n+1)]
#
#     # def add(self, point_inp): #замена названия функции и входящих данных
#     #     self.size_ += 1
#     #     self.tree_.insert(self.size_, point_inp)
#     #     self.pointers.insert(point_inp[1], self.size_)
#     #     self.up(self.size_)
#
#     def up(self,p):
#         while p>1 and self.tree_[p // 2][0] > self.tree_[p][0]: #замена знака сравнения и значений на магнитуду
#             self.tree_[p // 2], self.tree_[p] = self.tree_[p], self.tree_[p // 2]
#             self.pointers[self.tree_[p // 2][1]], self.pointers[self.tree_[p][1]] = self.pointers[self.tree_[p][1]], self.pointers[self.tree_[p // 2][1]]
#             p = p // 2
#
#     def down(self, p_ex):
#         while p_ex * 2 <= self.size_:
#             if p_ex * 2 == self.size_:
#                 min_idx = p_ex * 2 #замена названия переменной
#             elif self.tree_[p_ex*2][0] < self.tree_[p_ex*2+1][0]: #замена знака сравнения и значения на магнитуду
#                 min_idx = p_ex*2
#             else:
#                 min_idx = p_ex * 2 + 1
#             if self.tree_[p_ex][0] > self.tree_[min_idx][0]: #замена знака сравнения и значения на магнитуду
#                 self.tree_[p_ex], self.tree_[min_idx] = self.tree_[min_idx], self.tree_[p_ex]
#                 self.pointers[self.tree_[p_ex][1]], self.pointers[self.tree_[min_idx][1]] = self.pointers[self.tree_[min_idx][1]], self.pointers[self.tree_[p_ex][1]]
#             p_ex = min_idx
#
#
#     def replace(self, lenght, vertex_replace):
#         tree_place = self.pointers[vertex_replace]
#         self.tree_[tree_place] = (lenght, vertex_replace)
#         if tree_place > 2:
#             if lenght < self.tree_[tree_place // 2][0]:
#                 self.up(tree_place)
#             else:
#                 self.down(tree_place)
#
#     def extract(self):
#         value = self.tree_[1]
#         self.tree_[1] = self.tree_[self.size_]
#         self.pointers[self.tree_[self.size_][1]] = 1
#         self.size_ -= 1
#         self.down(1)
#         return value
#
# a = Heap(5)
#
# a.replace(4,5)
# print(a.extract())
# print(a.extract())
# a.replace(10,3)
# a.replace(8,3)
a = 8

for i in range(5):
    a-= 1
    if a<7:
        break
print(a)