import heapq as hq

city_num, bus_num = map(int, input().split())

edge_list = []

for _ in range(bus_num):
    u, v, uv_w = map(int, input().split())
    edge_list.append([u, v, uv_w]) # 인접리스트로 edge 표현
    
prev = [-1] * city_num
d = [float('inf')] * city_num
d[0] = 0 # start

for _ in range(city_num-1):
    for (u, v, w_uv) in edge_list:
        if d[u-1] + w_uv < d[v-1]:
            d[v-1] = d[u-1] +w_uv
            prev[v-1] = u

for (u, v, w_uv) in edge_list:
    if d[u-1] + w_uv < d[v-1]:
        print(-1)
        exit(0)

ans = '\n'.join(list(map(str, [i for i in d[1:]])))
print(ans.replace("inf", '-1'))
