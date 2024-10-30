import math

def mcm(p):
    n = len(p)
    dp = [[-1] * n for _ in range(n)]
    
    def S(s, e):
        if e - s == 1: return 0
        if dp[s][e] != -1: return dp[s][e]
        
        ans = math.inf
        for i in range(s+1, e):
            ans = min(ans, S(s,i) + S(i, e) + p[s]*p[i]*p[e])
        
        dp[s][e] = ans
        return ans
    
    return S(0, len(p)-1)

cnt = int(input())

matrix = []

for i in range(cnt):
    if i == cnt -1:
        matrix += input().split()
    else:
        matrix.append(input().split()[0])

matrix = list(map(int, matrix))

print(mcm(matrix))