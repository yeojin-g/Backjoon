cnt = int(input())
meeting_list = []

for i in range(cnt):
    meeting_time = list(map(int, input().split()))
    meeting_list.append(meeting_time)

meeting_list.sort(key=lambda x: (x[1], x[0]))

before_end = 0
meeting_cnt = 0

for meeting in meeting_list:
    if meeting[0] >= before_end:
        before_end = meeting[1]
        meeting_cnt += 1

print(meeting_cnt)
