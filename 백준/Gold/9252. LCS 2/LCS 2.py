import sys
input = sys.stdin.readline

a = [0] + list(input().rstrip())
b = [0] + list(input().rstrip())
dp = [['']*len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + a[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

result = dp[-1][-1]
print(str(len(result)) + '\n' + result)