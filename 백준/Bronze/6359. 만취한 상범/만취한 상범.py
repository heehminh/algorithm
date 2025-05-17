T = int(input())

for _ in range(T):
    N = int(input()) # 방의 개수
    ans = [1 for _ in range(N)]
    cnt = 1
    
    for i in range(N):
        cnt += 1 
        for j in range(cnt, N+1, cnt):
            if ans[j-1] == 1:
                ans[j-1] = 0 
            else:
                ans[j-1] = 1
                
    print(sum(ans))