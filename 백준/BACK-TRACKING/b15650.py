# 백준 15650 N과 M (2)

from itertools import combinations

N, M = map(int, input().split())

# arr을 만들기
arr = []
for i in range(N):
    arr.append(i+1)

for combi in combinations(arr, M):
    for i in combi:
        print(i, end=" ")
    print()