# 백준 10828 스택
import sys

stk = []
for _ in range(int(sys.stdin.readline())):
    method = sys.stdin.readline().split()
    
    if method[0] == "push":
        stk.append(method[1])
        
    elif method[0] == "pop":
        if stk:
            print(stk.pop())
        else:
            print(-1)
            
    elif method[0] == "size":
        print(len(stk))
        
    elif method[0] == "empty":
        print(1 if len(stk)==0 else 0)
        
    elif method[0] == "top":
        print(stk[-1] if stk else -1)
    
    
    