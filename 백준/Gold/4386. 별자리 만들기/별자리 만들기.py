import heapq  # 우선순위 큐 사용 - Prim (우선순위, 값)

star_num = int(input())

star_list = []
edge_heap = []
mst = set()  
total_cost = 0

for _ in range(star_num):
    star_xy = list(map(float, input().split()))
    star_list.append(star_xy)

# 초기화: 첫 번째 노드를 MST에 추가
mst.add(0)
st_x, st_y = star_list[0]

# 첫 번째 노드와 다른 모든 노드 간의 거리 계산하여 힙에 삽입
for i in range(1, star_num):
    x, y = star_list[i]
    distance = ((st_x - x) ** 2 + (st_y - y) ** 2) ** 0.5
    heapq.heappush(edge_heap, (distance, 0, i))  # (거리, u, v)

# MST가 완성될 때까지 반복
while len(mst) < star_num:
    cost, _, v = heapq.heappop(edge_heap)

    if v in mst:
        continue

    mst.add(v)
    total_cost += cost

    st_x, st_y = star_list[v]
    for i in range(star_num):
        if i not in mst: 
            x, y = star_list[i]
            distance = ((st_x - x) ** 2 + (st_y - y) ** 2) ** 0.5
            heapq.heappush(edge_heap, (distance, v, i)) 

print(f"{total_cost:.2f}")