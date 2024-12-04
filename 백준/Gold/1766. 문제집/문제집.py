import heapq as hq

q_num, info_num = map(int, input().split())

info_list = [[] for i in range(q_num)]

for _ in range(info_num): # 인접 리스트 생성
    a, b = map(int, input().split())
    
    info_list[a-1].append(b)
    
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
            hq.heappush(node_list, (u+1))
            
    #탐색
    while node_list:
        u = hq.heappop(node_list)
        result.append(u)
        
        for v in adj[u-1]:
            d[v-1] -= 1
            if d[v-1] == 0:
                hq.heappush(node_list, v)
                
    return result

print(' '.join(list(map(str, Kahns(info_list))))) 