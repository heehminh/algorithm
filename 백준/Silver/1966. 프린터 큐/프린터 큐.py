from collections import deque
import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    arr = list(map(int, input().split()))
    q = deque([i, arr[i]] for i in range(N)) # idx, 중요도
    
    ans = 0 
    
    while q:
        idx, p = q.popleft()
        
        # 현재 큐에 더 높은 중요도가 있는지 확인 
        if q and p < max(p for _, p in q):
            q.append([idx, p]) # 맨 뒤로 
        else:
            ans += 1 # 출력 
            if idx == M:
                print(ans)
                break 