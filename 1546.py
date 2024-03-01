l = int(input()) #len(list)
sList1 = input().split() # score list
sList2 = [int(i) for i in sList1] # str list to int list

bScore = max(sList2) # best score

for i in range(0,len(sList2)): # calc new score
    sList2[i] = sList2[i]/bScore*100

print(sum(sList2)/l) # print new average