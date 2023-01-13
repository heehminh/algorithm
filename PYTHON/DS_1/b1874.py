# 백준 1874 스택 수열 
import sys

stk = []
result = [] # 정답 +- 연산을 담은 리스트
num = 1 # 현재 숫자
isStack = True 

for _ in range(int(sys.stdin.readline())):
    P = int(sys.stdin.readline())
    
    # PUSH
    while num <= P:
        # 현재 스택에 P가 들어있지 않은 경우
        stk.append(num)
        result.append("+")
        num += 1 
        
    # POP
    if stk[-1] == P:
        stk.pop()
        result.append("-")
    
    # NO 
    else:
        isStack = False

if isStack:
    print("\n".join(result))
else:
    print("NO")