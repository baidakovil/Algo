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
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def rec_minim(self, pointer, search_L, search_R, seg_L, seg_R):

        if search_L == seg_L and search_R == seg_R:
            return self.tree[pointer]

        left_child_seg_R = (seg_R + seg_L) // 2

        if search_R <= left_child_seg_R:
            return self.rec_minim(pointer * 2, search_L, search_R, seg_L, left_child_seg_R)

        if search_L >= left_child_seg_R + 1:
            return self.rec_minim(pointer * 2 + 1, search_L, search_R, left_child_seg_R + 1, seg_R)

        return min(self.rec_minim(pointer * 2, search_L, left_child_seg_R, seg_L, left_child_seg_R),
                   self.rec_minim(pointer * 2 + 1, left_child_seg_R + 1, search_R, left_child_seg_R + 1, seg_R))

    def minim(self, l, r):
        return self.rec_minim(1, l, r, 0, self.base - 1)

line = open('input_Priority_queue.txt')
n, k = map(int, next(line).split())
N = tuple(map(int, next(line).split()))

a = Tree(N)

# for i in range(0, n-k+1):
#     print(a.minim(i, k-1))
#     k += 1

otvet = '\n'.join([str(a.minim(i, i+k-1)) for i in range(0, n-k+1)])
print(otvet)