n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0] * (n+1)

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

output = []
for _ in range(m):
    op, u, v = map(int, input().split())
    if op == 0:
        union(u, v)
    elif op == 1:
        if find_set(u) == find_set(v):
            output.append("YES")
        else:
            output.append("NO")

print("\n".join(output) + "\n")