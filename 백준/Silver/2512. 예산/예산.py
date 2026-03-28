# 백준 2512 예산 (파라메트릭 서치)
N = int(input())
req = list(map(int, input().split()))
M = int(input())

# 탐색 범위 설정
low = 0
high = max(req)
mid = (low+high)//2
ans = 0 

def is_possible(mid):
    return sum (min(r,mid) for r in req) <= M

while low <= high:
    if is_possible(mid):
        low = mid+1
        ans = mid 
    else:
        high = mid-1
    mid = (low+high) // 2
        
print(ans)