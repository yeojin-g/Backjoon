gd_num, route_num = map(int, input().split())

parent = [i for i in range(gd_num)]
rank = [0] * gd_num

def find_set(u):
    r = u
    while parent[r] != r:
        r = parent[r]
    while u != r:
        t = parent[u]
        parent[u] = r
        u = t
    return r  

def union(u, v):
    root_u = find_set(u)
    root_v = find_set(v)

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

gd_list = [tuple(map(int, input().split())) for _ in range(gd_num)]
edges = []
total_w = 0.0

for _ in range(route_num):
    u, v = map(int, input().split())
    union(u-1, v-1)

for i in range(gd_num):
    for j in range(i + 1, gd_num):
        weight = ((gd_list[i][0] - gd_list[j][0]) ** 2 + (gd_list[i][1] - gd_list[j][1]) ** 2) ** 0.5
        edges.append((i, j, weight))

edges.sort(key=lambda x: x[2])

for u, v, w in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        total_w += w

print(f"{total_w:.2f}")