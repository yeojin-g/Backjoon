# counting sort로 구현
import sys

def input():
    return sys.stdin.readline()

cnt = int(input()) # 입력 개수
cnt_arr = [0]*10001

for i in range(cnt):
    a = int(input())
    cnt_arr[a] += 1

for i in range(10001):
    if cnt_arr[i] != 0:
        for j in range(cnt_arr[i]):
            print(i)