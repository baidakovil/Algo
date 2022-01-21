import heapq
import math

line = open('input_DijkstraGraph.txt')
n, m = map(int, next(line).split())
# n, m = map(int, input().split())
if m == 0:
    print('-1')
vdata = tuple(dict(shortest = math.inf, final = False,
                   prev = None) for _ in range(n+1))
vdata[1]['shortest'] = 0
g_list = [[] for _ in range(n+1)]
shortest = [(math.inf,i) for i in range(2,n+1)]
shortest.insert(0, (0,1))

for i in range(m):
    v1, v2, w = map(int, next(line).split())
    # v1, v2, w = map(int, input().split())
    g_list[v1]=g_list[v1] + [(v2, w)]
    g_list[v2]=g_list[v2] + [(v1, w)]

g = tuple(tuple(g_list[i]) for i in range(n+1))

def Dijkstra(G,V):
    for _ in range(V):
        v = heapq.heappop(shortest)[1]
        v_info = vdata[v]
        edges = G[v]
        if not v_info['final']:
            if edges:
                for neigbo in edges:
                    if neigbo[0] == v:
                        continue
                    neigbo_info = vdata[neigbo[0]]
                    if not neigbo_info['final']:
                        try_shortest = v_info['shortest'] + neigbo[1]
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

no_path = reversed(Dijkstra(g,n))

print(*no_path)