N = int(input())
M = int(input())
S = input() 

ans = 0 
i = 0
cnt = 0 

while i < M-2:
    if S[i:i+3] == 'IOI':
        cnt += 1 
        i += 2 
        if cnt >= N:
            ans += 1 
            cnt -= 1 # 겹치는 경우 처리

    else:
        cnt = 0 
        i += 1 

print(ans)