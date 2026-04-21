from itertools import combinations_with_replacement
import math

N = int(input())

squares = [0] * (int(math.sqrt(N))) 
for i in range(len(squares)):
    squares[i] = (i+1)*(i+1)

for cnt in range(1, 4):
    for c in combinations_with_replacement(squares, cnt):
        if sum(c) == N:
            print(cnt)
            exit()

print(4)