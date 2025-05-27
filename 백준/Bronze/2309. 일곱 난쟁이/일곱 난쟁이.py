from itertools import combinations

arr = [int(input()) for _ in range(9)]

combi = list(combinations(arr, 7)) 

for i in combi:
    if sum(i) == 100:
        for height in sorted(list(i)):
            print(height)
        break
