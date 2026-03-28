from itertools import combinations
import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
str = list(input().rstrip())
ans = ''
isFound = False 

for c in combinations(str, M):
    if c[-1] not in ['A', 'E', 'I', 'O', 'U'] and c[M-2] == 'A' and c[M-3] == 'A':
        isFound = True 
        ans = c
        break 

if isFound:
    print('YES')
    print(''.join(ans))
else:
    print('NO')