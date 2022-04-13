# def priority_queue (n, k, N):
from typing import List

class Tree:
    def __init__(self, input):
        s = len(input)
        self.base = 1
        while self.base < s:
            self.base = self.base * 2
        self.tree = list()
        for _ in range(0, self.base * 2):
            self.tree.append(0)

        for i in range(0, s):
            self.tree[self.base + i] = input[i]

        for i in range(self.base - 1, 1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def __rec_summ(self, pointer, search_L, search_R, seg_L, seg_R):

        if search_L == seg_L and search_R == seg_R:
            return self.tree[pointer]

        left_child_seg_R = (seg_R + seg_L) // 2

        if search_R <= left_child_seg_R:
            return self.__rec_summ(pointer * 2, search_L, search_R, seg_L, left_child_seg_R)

        if search_L >= left_child_seg_R + 1:
            return self.__rec_summ(pointer * 2 + 1, search_L, search_R, left_child_seg_R + 1, seg_R)

        return self.__rec_summ(pointer * 2, search_L, left_child_seg_R, seg_L, left_child_seg_R) \
               + self.__rec_summ(pointer * 2 + 1, left_child_seg_R + 1, search_R, left_child_seg_R + 1, seg_R)

    def summ(self, l, r):
        return self.__rec_summ(1, l, r, 0, self.base - 1)

line = open('input_Priority_queue.txt')
n, k = map(int, next(line).split())
N = tuple(map(int, next(line).split()))

a = Tree(N)

for i in range(0, n-k+1):
    print(a.summ(i,k-1))
    k += 1