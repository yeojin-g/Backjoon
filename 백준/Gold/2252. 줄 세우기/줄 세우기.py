std_num, comp_num = map(int, input().split())

std_list = [[] for _ in range(std_num)]

for _ in range(comp_num): # 인접 리스트 생성
    a, b = map(int, input().split())
    
    std_list[a-1].append(b)
    
def Kahns(adj): # Kahn's Algorithm
    result = [] # return list
    node_list = [] # 진입 간선 없는 애들 저장
    n = len(adj) # 인접 리스트 len - 노드 수
    d = [0] * n #  진입 간선 수 저장
    
    # 초기화
    for u in range(n):
        for v in adj[u]:
            d[v-1] += 1
            
    for u in range(n):
        if d[u] == 0:
            node_list.append(u+1)
            
    #탐색
    while node_list:
        u = node_list.pop(0)
        result.append(u)
        
        for v in adj[u-1]:
            d[v-1] -= 1
            if d[v-1] == 0:
                node_list.append(v)
                
    return result

print(' '.join(list(map(str, Kahns(std_list)))))     