import heapq as hq

city_num = int(input())
bus_num = int(input())

edge_list = [[] for i in range(city_num)]

for _ in range(bus_num):
    u, v, uv_w = map(int, input().split())
    edge_list[u-1].append([v, uv_w]) # 인접리스트로 edge 표현
    
prev = [-1] * city_num
d = [float('inf')] * city_num
st_node, end_node = map(int, input().split())
d[st_node-1] = 0 # start

S = set()
Q = []
hq.heappush(Q, (0, st_node))

while Q:
    w, u = hq.heappop(Q)
    if u in S: continue
    S.add(u)
    
    for v, w_uv in edge_list[u-1]: # neighbors
        if v not in S and d[u-1] + w_uv < d[v-1]:
            d[v-1] = d[u-1] + w_uv
            prev[v-1] = u
            hq.heappush(Q, (d[v-1], v))
            
total_cost = d[end_node-1]            
print(total_cost) 