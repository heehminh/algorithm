# 백준 19637 
# 이분탐색 
# names: WEAK, .. , A 
# powers: 10000

import sys 
from bisect import bisect_left

N, M = map(int, sys.stdin.readline().split())

names = []
powers = []

for _ in range(N):
    name, power = sys.stdin.readline().split()
    names.append(name)
    powers.append(int(power))
    
arr = [int(sys.stdin.readline()) for _ in range(M)]
for i in arr:
    print(names[bisect_left(powers, i)])