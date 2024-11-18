test_cnt = int(input())
ans = []

for _ in range(test_cnt):
    cand_cnt = int(input())
    score_list = []
    cnt = 1
    
    for _ in range(cand_cnt):
        score_list.append(list(map(int, input().split())))
    
    score_list.sort(key = lambda x: x[0])
    
    bef_score = score_list[0][1]
    for i in range(1, cand_cnt):
        if bef_score > score_list[i][1]:
            cnt += 1
            bef_score = score_list[i][1]
            
    ans.append(str(cnt))
    
print('\n'.join(ans))