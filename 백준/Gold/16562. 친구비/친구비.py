std, rel, money = map(int, input().split())

mon_list = list(map(int, input().split()))

parent = [i for i in range(std)]
rank = [0] * std

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
        # 친구비 비교로 root 결정
        if mon_list[root_u] < mon_list[root_v]: 
            parent[root_v] = root_u
        elif mon_list[root_u] > mon_list[root_v]: 
            parent[root_u] = root_v
        else:
            # 친구비가 같다면 기존 방식으로
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

for _ in range(rel):
    a, b = map(int, input().split())
    union(a-1, b-1)    

set_cnt = set(find_set(i) for i in range(std))

total_cost = sum(mon_list[i] for i in set_cnt)

if total_cost > money:
    print("Oh no")
else:
    print(total_cost)