from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0 

for i in combinations(cards, 3):
    i_sum = sum(i)
    if result < i_sum <= M:
        result = i_sum
print(result)