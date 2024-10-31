import sys

cnt = int(input())
arr = list(map(int, input().rstrip().split(" ")))

dp = [1] * cnt

for i in range(cnt):
    for j in range(i):
        if (arr[j] < arr[i]):
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))