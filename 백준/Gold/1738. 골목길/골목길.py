city_num, edge_num = map(int, input().split())

edge_list = []

for _ in range(edge_num):
    u, v, uv_w = map(int, input().split())
    edge_list.append([u, v, uv_w])

prev = [-1] * (city_num + 1)
d = [-float('inf')] * (city_num + 1)
d[1] = 0

for i in range(city_num):
    for u, v, w_uv in edge_list:
        if d[u] != -float('inf') and d[u] + w_uv > d[v]:
            d[v] = d[u] + w_uv
            prev[v] = u
            if i == city_num - 1:  
                # 마지막 라운드에서 음의 사이클이 있는 경우
                # 교안엔 for문을 아예 따로 빼서 하나 더 만들었었음
                d[v] = float('inf')  

# 음의 사이클 감지 여부
visited = [False] * (city_num + 1)

def detect_cycle(node):
    if visited[node]:
        return True
    visited[node] = True
    if prev[node] != -1 and detect_cycle(prev[node]):
        return True
    visited[node] = False
    return False

if detect_cycle(city_num):
    print(-1)
else:
    path = []
    current = city_num
    while current != -1:
        path.append(current)
        current = prev[current]

    if path[-1] != 1:  # 시작점으로 도달하지 못한 경우
        print(-1)
    else:
        path.reverse()
        print(' '.join(map(str, path)))
