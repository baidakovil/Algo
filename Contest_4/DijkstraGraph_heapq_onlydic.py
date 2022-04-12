import math

class Heap:
    def __init__(self, n):
        self.tree_ = [(math.inf,i) for i in range(1,n+1)]
        self.tree[0] = (0,1)
        self.size_ = len(self.tree_)-1

    def add(self, point_inp): #замена названия функции и входящих данных
        self.size_ += 1
        self.tree_.insert(self.size_, point_inp)
        p = self.size_
        while p>1 and self.tree_[p // 2][1] > self.tree_[p][1]: #замена знака сравнения и значений на магнитуду
            self.tree_[p // 2], self.tree_[p] = self.tree_[p], self.tree_[p // 2]
            p = p // 2

    def extract(self):
        value = self.tree_[1]
        self.tree_[1] = self.tree_[self.size_]
        self.size_ -= 1
        p_ex = 1
        while p_ex * 2 <= self.size_:
            if p_ex * 2 == self.size_:
                min_idx = p_ex * 2 #замена названия переменной
            elif self.tree_[p_ex*2][1] < self.tree_[p_ex*2+1][1]: #замена знака сравнения и значения на магнитуду
                min_idx = p_ex*2
            else:
                min_idx = p_ex * 2 + 1
            if self.tree_[p_ex][1] > self.tree_[min_idx][1]: #замена знака сравнения и значения на магнитуду
                self.tree_[p_ex], self.tree_[min_idx] = self.tree_[min_idx], self.tree_[p_ex]
            p_ex = min_idx
        return value

# line = open('input_DijkstraGraph.txt')
# n, m = map(int, next(line).split())
n, m = map(int, input().split())

shortest = Heap(n)
final = dict.fromkeys(range(1, n+1), False)
prev = dict.fromkeys(range(1, n+1), None)
g = dict.fromkeys(range(1, n + 1), [])


short_all[1] = 0
added = False

for i in range(m):
    # v1, v2, w = map(int, next(line).split())
    v1, v2, w = map(int, input().split())
    if v1 == v2:
        continue
    g[v1]= g[v1] + [(v2, w)]
    g[v2]= g[v2] + [(v1, w)]

while not all(final.values()):
    v = heapq.heappop(shortest)[1]
    edges = g[v]
    if not final[v] and edges:
        for neigbo in edges:
            try_shortest = short_all[v] + neigbo[1]
            if (not final[neigbo[0]]) and (try_shortest < short_all[neigbo[0]]):
                short_all[neigbo[0]] = try_shortest
                for i in range(len(shortest)):
                    if shortest[i][1] == neigbo[0]:
                        shortest[i] = (try_shortest, neigbo[0])
                        heapq.heapify(shortest)
                        added = True
                if added:
                    added = False
                else:
                    heapq.heappush(shortest, (try_shortest, neigbo[0]))
                prev[neigbo[0]] = v
    final[v] = True
    if v == n:
        break

path = [n]
dot = n

while dot > 1:
    dot = prev[dot]
    if dot is None:
        path = [-1]
        break
    path.append(dot)

if path[-1] != 1:
    path = [-1]

print(*reversed(path))