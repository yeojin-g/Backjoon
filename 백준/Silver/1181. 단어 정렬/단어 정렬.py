wordsCnt = int(input())  # 단어 개수
wordList = []

for i in range(wordsCnt):
    word = input()
    
    if word not in wordList:  # 중복 단어는 제외
        wordList.append(word)

# 단어를 길이순으로 먼저 정렬하고, 길이가 같으면 알파벳 순으로 정렬
wordList.sort(key=lambda x: (len(x), x))

print("\n".join(wordList))
