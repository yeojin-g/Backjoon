import heapq as hq

stud_num, edge_num, st_town = map(int, input().split())

edge_list = [[] for i in range(stud_num)]
reverse_edge_list = [[] for i in range(stud_num)]

for _ in range(edge_num):
    u, v, uv_w = map(int, input().split())
    edge_list[u-1].append([v, uv_w]) # 인접리스트로 edge 표현
    reverse_edge_list[v-1].append([u,uv_w]) # 역방향 리스트
    
prev = [-1] * stud_num
d = [float('inf')] * stud_num
d[st_town-1] = 0 # start

S = set()
S_reverse = set()
Q = []
hq.heappush(Q, (0, st_town))

while Q:
    w, u = hq.heappop(Q)
    if u in S: continue
    S.add(u)
    
    for v, w_uv in edge_list[u-1]: # neighbors
        if v not in S and d[u-1] + w_uv < d[v-1]:
            d[v-1] = d[u-1] + w_uv
            prev[v-1] = u
            hq.heappush(Q, (d[v-1], v))

prev_reverse = [-1] * stud_num
d_reverse = [float('inf')] * stud_num
d_reverse[st_town-1] = 0 # start

S_reverse = set()   
hq.heappush(Q, (0, st_town))
        
while Q:
    w, u = hq.heappop(Q)
    if u in S_reverse: continue
    S_reverse.add(u)
    
    for v, w_uv in reverse_edge_list[u-1]: # neighbors
        if v not in S_reverse and d_reverse[u-1] + w_uv < d_reverse[v-1]:
            d_reverse[v-1] = d_reverse[u-1] + w_uv
            prev_reverse[v-1] = u
            hq.heappush(Q, (d_reverse[v-1], v))
            
        
for i in range(len(d_reverse)):
    d[i] += d_reverse[i]
    
# max_idx = max(enumerate(d), key=lambda x: x[1])[0] # enumerate (idx:value) - 이건 그 학생의 번호 출력하는 것
print(max(d))