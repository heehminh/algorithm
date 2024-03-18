# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로 
# 중복된 단어는 하나만 남기고 제거 

N = int(input())
words = []

for _ in range(N):
    words.append(input())
    
res = list(set(words))
res.sort() # 사전순으로
res.sort(key=len) # 단어길이순으로

for word in res:
    print(word)