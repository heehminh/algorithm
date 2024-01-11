# 백준 3986 좋은 단어
N = int(input())

cnt = 0
for _ in range(N):
    word = input()
    stk = []
    
    for i in word:
        if len(stk) == 0:
            stk.append(i)
        else:
            if stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
                
    if len(stk) == 0:
        cnt += 1
        
print(cnt)