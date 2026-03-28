# 백준 3986 좋은 단어
import sys

N = int(sys.stdin.readline())

cnt = 0
for _ in range(N):
    str = sys.stdin.readline().rstrip()
    stk = []
    
    for i in str:
        if len(stk) == 0:
            stk.append(i)
        else: 
            if stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
    
    if len(stk)==0:
        cnt += 1
        
print(cnt)