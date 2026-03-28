from collections import defaultdict 
import sys 
input = sys.stdin.readline 

N, D, K, C = map(int, input().split()) 
arr = [int(input()) for _ in range(N)]
count = [0] * (D+1) # 각 초밥 번호 개수 
kind = 0 # 현재 윈도우 안의 서로 다른 초밥 수 

for i in range(K):
    if count[arr[i]] == 0:
        kind += 1 
    count[arr[i]] += 1 

ans = kind 
if count[C] == 0:
    ans += 1 

# 슬라이딩 윈도우
for i in range(1, N):
    left = arr[i-1] # 빠지는 초밥
    right = arr[(i+K-1) % N] # 새로 들어오는 초밥 
    
    count[left] -= 1 
    if count[left] == 0:
        kind -= 1 
    
    if count[right] == 0:
        kind += 1
    count[right] += 1 
    
    temp = kind 
    if count[C] == 0:
        temp += 1 
    
    ans = max(temp, ans)
    
print(ans)