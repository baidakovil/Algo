import heapq, math, numpy as np

# line = open('input_DijkstraGraph.txt')
# n, m = map(int, next(line).split())
n, m = map(int, input().split())
if m == 0:
    print('-1')
vdata = tuple(dict(shortest = math.inf, final = False,
                   prev = None) for _ in range(n+1))
vdata[1]['shortest'] = 0
shortest = [(math.inf,i) for i in range(2,n+1)]
shortest.insert(0, (0,1))

g_array = np.zeros([n+1,n+1],dtype=int)
for i in range(m):
    data = tuple(map(int, input().split()))
    # data = tuple(map(int, next(line).split()))
    v1, v2, w = data[0], data[1], data[2]
    if v1 == v2:
        continue
    cell_1, cell_2 = g_array[v1, v2], g_array[v2, v1]
    if cell_1 == 0:
        g_array[v1, v2], g_array[v2, v1] = w, w
    else:
        choice = min(cell_1, w)
        g_array[v1, v2], g_array[v2, v1] = choice, choice

del i, data, v1, v2, w, m

def Dijkstra(G,V):
    for _ in range(V):
        v = heapq.heappop(shortest)[1]
        v_info = vdata[v]
        edges = np.transpose((G[v] > 0).nonzero())
        if not v_info['final']:
            if len(edges):
                for neigbo in edges:
                    neigbo_info = vdata[neigbo[0]]
                    if not neigbo_info['final']:
                        try_shortest = v_info['shortest'] + G[v, neigbo[0]]
                        if try_shortest < neigbo_info['shortest']:
                            neigbo_info['shortest'] = try_shortest
                            heapq.heappush(shortest, (try_shortest, neigbo[0]))
                            neigbo_info['prev'] = v
            v_info['final'] = True
            if v == n:
                break
    path = [n]
    dot = n
    while dot > 1:
        dot = vdata[dot]['prev']
        if dot is None:
            return [-1]
        path.append(dot)
        if dot == 1:
            return path
    return [-1]

no_path = Dijkstra(g_array,n)
print(*no_path[::-1])