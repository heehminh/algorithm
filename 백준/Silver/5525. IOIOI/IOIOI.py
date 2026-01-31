N = int(input())
M = int(input())
S = input() 

str = 'I'
for i in range(N):
    str += 'OI'

ans = 0 
for i in range(M-len(str)+1):
    
    if str == S[i:i+len(str)]:
        ans += 1 

print(ans)