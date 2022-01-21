import math

class Heap:
    def __init__(self, n):
        self.tree_ = [(math.inf,j) for j in range(0,n+1)]
        self.tree_[0] = (0, 0)
        self.tree_[1] = (0,1)
        self.size_ = len(self.tree_)-1
        self.pointers = [k for k in range(0,n+1)]

    def up(self,p):
        while p>1 and self.tree_[p // 2][0] > self.tree_[p][0]: #замена знака сравнения и значений на магнитуду
            self.tree_[p // 2], self.tree_[p] = self.tree_[p], self.tree_[p // 2]
            self.pointers[self.tree_[p // 2][1]], self.pointers[self.tree_[p][1]] = self.pointers[self.tree_[p][1]], self.pointers[self.tree_[p // 2][1]]
            p = p // 2

    def down(self, p_ex):
        while p_ex * 2 <= self.size_:
            if p_ex * 2 == self.size_:
                min_idx = p_ex * 2 #замена названия переменной
            elif self.tree_[p_ex*2][0] < self.tree_[p_ex*2+1][0]: #замена знака сравнения и значения на магнитуду
                min_idx = p_ex*2
            else:
                min_idx = p_ex * 2 + 1
            if self.tree_[p_ex][0] > self.tree_[min_idx][0]: #замена знака сравнения и значения на магнитуду
                self.tree_[p_ex], self.tree_[min_idx] = self.tree_[min_idx], self.tree_[p_ex]
                self.pointers[self.tree_[p_ex][1]], self.pointers[self.tree_[min_idx][1]] = self.pointers[self.tree_[min_idx][1]], self.pointers[self.tree_[p_ex][1]]
            p_ex = min_idx

    def replace(self, lenght, vertex_replace):
        tree_place = self.pointers[vertex_replace]
        self.tree_[tree_place] = (lenght, vertex_replace)
        if lenght < self.tree_[tree_place // 2][0]:
            self.up(tree_place)
        else:
            self.down(tree_place)

    def extract(self):
        value = self.tree_[1]
        if self.size_ == 1:
            return 0,0
        self.tree_[1] = self.tree_[self.size_]
        self.pointers[self.tree_[self.size_][1]] = 1
        self.size_ -= 1
        self.down(1)
        return value

    def read_len(self, vertex_read):
        value = self.tree_[self.pointers[vertex_read]][0]
        return value

# line = open('input_DijkstraGraph.txt')
# n, m = map(int, next(line).split(' '))
n, m = map(int, input().split())

shortest = Heap(n)
final = [False] * (n+1)
prev = [None] * (n+1)
g_list = [[]] * (n+1)

for i in range(m):
    # v1, v2, w = map(int, next(line).split(' '))
    v1, v2, w = map(int, input().split(' '))
    if v1 == v2:
        continue
    g_list[v1]= g_list[v1] + [(v2, w)]
    g_list[v2]= g_list[v2] + [(v1, w)]

g = tuple(tuple(g_list[i]) for i in range(n+1))
del g_list, v1, v2, w, m

for i in range(n):
    v_len, v = shortest.extract()
    if (v_len == 0) and (v == 0):
        break
    edges = g[v]
    if not final[v] and edges:
        for neigbo in edges:
            try_shortest = v_len + neigbo[1]
            if (not final[neigbo[0]]) and (try_shortest < shortest.read_len(neigbo[0])):
                shortest.replace(try_shortest, neigbo[0])
                prev[neigbo[0]] = v
    final[v] = True
    if (v == n) or (all(final)):
        break

path = [n]
dot = n

for _ in range(n):
    dot = prev[dot]
    if dot is None:
        path = [-1]
        break
    path.append(dot)
    if dot == 1:
        break

if path[-1] != 1:
    path = [-1]

print(*reversed(path))