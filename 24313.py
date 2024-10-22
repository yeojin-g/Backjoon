a1, a0 = list(map(int, input().split()))  # [a1, a0]
c = int(input())
n0 = int(input())
pr = 1

for i in range(n0, 100):
    ans = (a1*i+a0 <= c*i)
    if not ans:
        pr = 0
        break
print(pr)