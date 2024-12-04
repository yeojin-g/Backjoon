import heapq as hq

def Kahns(adj, order):
    result = []        # 최종 순위를 저장할 리스트
    node_list = []     # 진입 간선이 없는 노드를 저장할 힙
    n = len(adj)       # 노드의 수
    d = [0] * n        # 각 노드의 진입 차수를 저장할 리스트

    # 진입 차수 계산
    for u in range(n):
        for v in adj[u]:
            d[v] += 1

    # 초기화: 진입 차수가 0인 노드를 힙에 추가 (순위 기준으로 우선순위 설정)
    for u in range(n):
        if d[u] == 0:
            hq.heappush(node_list, (order[u], u))

    # 위상 정렬 수행
    while node_list:
        # 진입 차수가 0인 노드가 여러 개일 경우, 순위를 확정할 수 없음
        if len(node_list) > 1:
            return "?"

        _, u = hq.heappop(node_list)  # 순위가 가장 높은 노드 선택
        result.append(u + 1)          # 결과 리스트에 추가 (1-based 인덱스)

        # 선택된 노드와 연결된 간선 제거
        for v in adj[u]:
            d[v] -= 1
            if d[v] == 0:
                hq.heappush(node_list, (order[v], v))

    # 모든 노드를 방문하지 못했으면 사이클이 존재함
    if len(result) < n:
        return "IMPOSSIBLE"

    return result

# 입력 처리
testcase = int(input())
for _ in range(testcase):
    team_num = int(input())                   # 팀의 수
    rate_list = list(map(int, input().split()))  # 작년 순위 (높은 순서대로)
    pair_num = int(input())                   # 순위 변경 쌍의 수
    swap_list = [[] for _ in range(team_num)] # 인접 리스트 초기화

    # 각 팀의 초기 순위를 저장 (팀 번호를 0-based로)
    order = {team - 1: idx for idx, team in enumerate(rate_list)}

    # 초기 순위를 바탕으로 간선 설정 (높은 순위에서 낮은 순위로)
    for i in range(team_num):
        for j in range(i + 1, team_num):
            higher = rate_list[i] - 1
            lower = rate_list[j] - 1
            swap_list[higher].append(lower)

    # 순위 변경 정보 반영
    for _ in range(pair_num):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        # 기존 간선 방향 반전
        if b in swap_list[a]:
            swap_list[a].remove(b)
            swap_list[b].append(a)
        else:
            swap_list[b].remove(a)
            swap_list[a].append(b)

    # Kahn's Algorithm 실행 및 결과 출력
    result = Kahns(swap_list, order)
    if isinstance(result, list):
        print(" ".join(map(str, result)))
    else:
        print(result)
