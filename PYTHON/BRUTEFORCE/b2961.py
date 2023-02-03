# 백준 2961번 도영이가 만든 맛있는 음식
# 재료의 개수 N
# 각 재료의 신맛 S 쓴맛 B

# 1
# 3 10 -> 신맛: 3, 쓴맛: 10 = 7

# 2 
# 3 8
# 5 8
# 신맛: 3*5 쓴맛: 8+8 = 1

# 4
# (A): 6
# (B): 4
# (C): 5
# (D): 5
# (A, B): 11
# (A, C): 12
# (A, D): 12
# (B, C): 8
# (B, D): 5
# (C, D): 5
# (A, B, C): 15
# (A, B, D): 14
# (A, C, D): 12
# (B, C, D): 1 => 최적해 
# (A, B, C, D): 6

import sys 
from itertools import combinations
N = int(sys.stdin.readline())
matters = []

for _ in range(N):
    matters.append(list(map(int, sys.stdin.readline().split())))
   
com = []
for i in range(N):
    com.append(combinations(matters, i+1))
    
ans = 1_000_000_000

for i in com:
    # 몇개짜리 조합인지 
    for j in i:
        S = 1
        B = 0
        for e in j:
            S *= e[0]
            B += e[1]
        
        ans = min(ans, abs(S-B))
print(ans)