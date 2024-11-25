test = int(input())

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

for _ in range(test):
    camp_num = int(input())
    camp_list = []
    parent = [i for i in range(camp_num)]
    rank = [0] * camp_num
    for _ in range(camp_num):
        x, y, r = map(int, input().split())
        camp_list.append([x, y, r])
    
    for i in range(camp_num-1):
        for j in range(i+1, camp_num):
            x1, y1, r1 = camp_list[i]
            x2, y2, r2 = camp_list[j]
            if (x1-x2)**2 + (y1-y2)**2 <= (r1 + r2)**2: # 두 영역이 겹치는 경우
                union(i, j)
            
    set_cnt = len(set(find_set(i) for i in range(camp_num)))
    print(set_cnt)   