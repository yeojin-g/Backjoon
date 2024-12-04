import heapq as hq

def Kahns_weighted(adj, const_times, dest):  # Kahn's Algorithm
    result = [0] * len(adj)  # 각 건물까지의 최소 시간 저장
    in_degree = [0] * len(adj)  
    node_list = []  
    
    # 초기화
    for u in range(len(adj)):
        for v in adj[u]:
            in_degree[v] += 1

    for u in range(len(adj)):
        if in_degree[u] == 0:
            hq.heappush(node_list, (const_times[u], u))  # 비용 기준 최소 힙

    # 탐색
    while node_list:
        current_time, u = hq.heappop(node_list)  # 현재 건물 및 걸린 시간
        result[u] = current_time

        for v in adj[u]:  # 다음 건물들
            in_degree[v] -= 1
            if in_degree[v] == 0:
                hq.heappush(node_list, (current_time + const_times[v], v))
    
    return result[dest]

# 입력 처리
test_case = int(input())

for _ in range(test_case):
    build_num, const_rule = map(int, input().split())
    const_times = list(map(int, input().split()))
    build_list = [[] for _ in range(build_num)]
    
    for _ in range(const_rule):  # 인접 리스트 생성
        a, b = map(int, input().split())
        build_list[a - 1].append(b - 1) 
    
    dest_build = int(input()) - 1 
    print(Kahns_weighted(build_list, const_times, dest_build))