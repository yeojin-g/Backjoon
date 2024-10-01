nums = str(input())
arr = []
for i in range(0, len(nums)):
    arr.append(nums[i])

arr.sort(reverse=True)
ans = ''

for i in arr:
    ans += i
    
print(int(ans))