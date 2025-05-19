import math 

A, B, C = map(int, input().split())
T = int(input())

ans = 0 

# 30분 이하 A원 
# 30분 초과 B분마다 C원 
# 올림 

if T-30 >= 0:
    T -= 30 
    ans += A 
    
    ans += math.ceil(T/B)*C 
    print(ans)
    
else:
    print(A)