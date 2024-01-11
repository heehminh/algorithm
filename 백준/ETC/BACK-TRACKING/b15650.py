# 백준 15650 N과 M (2)
# 고른 수열은 오름차순이어야 한다. 
# 중복하는 수열을 여러 번 출력하면 안된다. 

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