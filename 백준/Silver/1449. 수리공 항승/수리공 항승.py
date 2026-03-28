# 백준 1449 수리공 항승
# N: 물이 새는 곳의 개수 L: 테이프의 길이 
# for _ in range(N): 물이 새는 곳의 위치 
# 위치 +1 

import sys 
N, L = map(int, sys.stdin.readline().split())
locations = list(map(int, sys.stdin.readline().split()))

locations.sort()

start = locations[0] 
ans = 1

for location in locations[1:]:
    if location in range(start, start+L):
        continue
    else:
        start = location
        ans += 1 
print(ans)