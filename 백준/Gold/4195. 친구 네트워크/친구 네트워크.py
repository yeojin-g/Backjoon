case_num = int(input())

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
            size[root_u] += size[root_v]  # root_u가 대표가 됨
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
            size[root_v] += size[root_u]  # root_v가 대표가 됨
        else:
            parent[root_v] = root_u
            rank[root_u] += 1
            size[root_u] += size[root_v]  # root_u가 대표가 됨
    
    # 합쳐진 집합의 크기 출력
    print(size[find_set(u)])

for _ in range(case_num):
    friend_num = int(input())
    friend_dict = {}
    parent = [i for i in range(friend_num * 2)]
    rank = [0] * (friend_num * 2)
    size = [1] * (friend_num * 2)  # 초기화: 모든 노드는 크기 1로 시작
    
    for _ in range(friend_num):
        a, b = input().split()
        
        if a not in friend_dict:
            friend_dict[a] = len(friend_dict)
        if b not in friend_dict:
            friend_dict[b] = len(friend_dict)
            
        a_num = friend_dict[a]
        b_num = friend_dict[b]
        
        union(a_num, b_num)