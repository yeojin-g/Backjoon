count = int(input()) # 횟수 입력 받음
pList = [] # 프린트 할 리스트
for i in range(0,count):
    iList = input().split() # 두 수 입력 받음
    s = int(iList[0]) + int(iList[1]) # sum
    pList.append(f"Case #{i+1}: {s}") # append in list
print('\n'.join(pList))

