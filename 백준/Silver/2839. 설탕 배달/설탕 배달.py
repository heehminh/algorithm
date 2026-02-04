N = int(input())

ans = 0 
i = int(N/5)

while i >= 0:
    n = N - (5*i)     
    ans = i
    
    if n == 0 or n % 3 == 0:
        ans += int(n/3)
        break 
    
    else:
        i -= 1 

print(ans) if ans > 0 else print(-1)