node, edge = map(int, input().split())

parent = [i for i in range(node)]
rank = [0] * node

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

edges = []
total_w = 0

for _ in range(edge): # Kruskal's Algorithm
    u, v, weight = map(int, input().split())
    edges.append([u, v, weight])

edges.sort(key=lambda x:x[2])

for u, v, w in edges:
    if find_set(u-1) != find_set(v-1):
        union(u-1, v-1)
        total_w += w
        
print(total_w)