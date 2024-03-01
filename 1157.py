word = input().upper() # 대소문자 구분 없도록 모두 대문자로 
alDic = {} # 알파벳 별 cnt 저장할 dic
ans = '' # 최종 answer

for i in word: # word 알파벳 별 count dictionary make
    if i not in alDic:
        alDic[i] = word.count(i)

maxCount = max(alDic.values()) # 최대 개수 

for i in alDic.keys(): # 최대 개수인 알파벳 여러개인지 판단
    if alDic[i] == maxCount:
        if ans != '':
            ans = '?'
            break
        else: 
            ans = i
print(ans)

