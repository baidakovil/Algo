import heapq, math

# line = open('input_DijkstraGraph.txt')
# n, m = map(int, next(line).split())
n, m = map(int, input().split())

short_all = dict.fromkeys(range(1, n+1), math.inf)
final = dict.fromkeys(range(1, n+1), False)
prev = dict.fromkeys(range(1, n+1), None)
# g_list = [[]] * (n+1)
g = dict.fromkeys(range(1, n + 1), [])

shortest = [(math.inf,i) for i in range(2,n+1)]
shortest.insert(0, (0,1))
short_all[1] = 0

for i in range(m):
    # v1, v2, w = map(int, next(line).split())
    v1, v2, w = map(int, input().split())
    if v1 == v2:
        continue
    g[v1]= g[v1] + [(v2, w)]
    g[v2]= g[v2] + [(v1, w)]

# g = tuple(tuple(g_dict[i]) for i in range(n + 1))

for _ in range(n):
    v = heapq.heappop(shortest)[1]
    edges = g[v]
    if not final[v] and edges:
        for neigbo in edges:
            try_shortest = short_all[v] + neigbo[1]
            if (not final[neigbo[0]]) and (try_shortest < short_all[neigbo[0]]):
                short_all[neigbo[0]] = try_shortest
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
    if dot == 1:
        break

if path[-1] != 1:
    path = [-1]

print(*reversed(path))