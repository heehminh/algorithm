import sys 

N = int(sys.stdin.readline())
s = []

for _ in range(N):
    str = sys.stdin.readline().split()
    
    if (str[0] == 'pop'):
        if s: print(s.pop())
        else: print(-1)
    
    elif (str[0] == 'size'):
        print(len(s))
        
    elif (str[0] == 'empty'):
        if s: print(0)
        else: print(1)
    
    elif (str[0] == 'top'):
        if s: print(s[-1])
        else: print(-1)
    
    elif (str[0] == 'push'):
        s.append(str[1])
