class Heap:
    def __init__(self):
        self.tree_ = list('0')
        self.size_ = len(self.tree_)-1

    def add(self, point_inp): #замена названия функции и входящих данных
        self.size_ += 1
        self.tree_.insert(self.size_, point_inp)
        p = self.size_
        while p>1 and self.tree_[p // 2][1] > self.tree_[p][1]: #замена знака сравнения и значений на магнитуду
            self.tree_[p // 2], self.tree_[p] = self.tree_[p], self.tree_[p // 2]
            p = p // 2

    def minima(self):
        if self.size_ == 0:
            return 'nono'
        return self.tree_[1]

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

class VData:
    def __init__(self, vertex_and_weight):
        self.edges = [vertex_and_weight]
        self.shortest = 99999999
        self.final = False
        self.prev = None
    def add(self, new_data):
        self.edges.append(new_data)

line = open('input_DijkstraGraph.txt')
n, m = map(int, next(line).split())
# n, m = map(int, input().split())
graph = [0 for i in range(n+1)]
shortest = Heap()

for i in range(m):
    data = list(map(int, next(line).split()))
    # data = list(map(int, input().split()))
    current = data[0]
    to_vertex = data[1:]
    if graph[current]:
        graph[current].add(to_vertex)
    else:
        graph[current]=VData(to_vertex)

for i in range(n+1):
    if graph[i] == 0:
        graph[i] = VData(())


def going(G,V):
    for i in range(V):
        vertex_w_min_path = int(shortest.extract()[0])
        if (not G[vertex_w_min_path].final) and (G[vertex_w_min_path].edges != [()]):
            relax(G, vertex_w_min_path)
            G[vertex_w_min_path].final = True

def relax(G, vertex_relax):
    for neigbo in G[vertex_relax].edges:
        if neigbo[0] == vertex_relax:
            continue
        try_shortest = G[vertex_relax].shortest + neigbo[1]
        if (not G[neigbo[0]].final) and (try_shortest < G[neigbo[0]].shortest):
            G[neigbo[0]].shortest = try_shortest
            shortest.add((neigbo[0],try_shortest))
            G[neigbo[0]].prev = vertex_relax

def Dijkstra(G,V):
    shortest.add((1,0))
    for i in range(2,V+1):
        shortest.add((V,99999999))
    G[1].shortest = 0
    for i in range(1, V):
        queue = shortest.minima()
        if (not queue == 'nono') and (not G[queue[0]].final):
            going(G,V)
    path = [n]
    dot = n
    for i in range (n,1,-1):
        dot = G[dot].prev
        if dot is None:
            return [-1]
        path.append(dot)
        if dot == 1:
            return path
    return [-1]

print(*Dijkstra(graph,n)[::-1])