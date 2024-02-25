n = int(input()) # 반복 횟수
pr = "" # 출력
for i in range(1,n+1):
    for j in range(0, i):
        pr += "*"
    pr += '\n'
print(pr)
