import sys
from itertools import combinations

N, max_number = map(int, input().split())
arr = list(map(int, input().split()))

result_number = 0

for combi in combinations(arr, 3):
    sum_number = sum(combi)
    if result_number < sum_number <= max_number:
        result_number = sum_number
    
print(result_number)