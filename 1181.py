wordsCnt = int(input())  # 단어 개수
wordList = []

for i in range(wordsCnt):
    word = input()
    
    if len(wordList) == 0:  # 첫 단어는 무조건 추가
        wordList.append(word)
    else:
        ins = False
        for j in range(len(wordList)):
            if len(word) < len(wordList[j]) or (len(word) == len(wordList[j]) and word < wordList[j]):
                wordList.insert(j, word)
                ins = True
                break     
        if not ins:
            wordList.append(word)

wordSet = set(wordList)
print()
print("\n".join(wordList))
print()
print("\n".join(wordSet))