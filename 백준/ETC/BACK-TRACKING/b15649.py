# 백준 15649 N과 M (1) 백트래킹 
# N, M (길이가 M인 수열)
# 1부터 N까지의 자연수 중에서 중복없이 M개를 고른 수열 
# 테스트케이스(1) 3, 1
# 1
# 2
# 3 

from itertools import permutations

N, M = map(int, input().split())

# arr을 만들기
arr = []
for i in range(N):
    arr.append(i+1)

for combi in permutations(arr, M):
    for i in combi:
        print(i, end=" ")
    print()