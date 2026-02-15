# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다.
import math

N = int(input())
squares = [i*i for i in range(1, int(math.sqrt(N))+1)] 

if N in squares:
    print(1)
    exit()

for a in squares:
    if N-a in squares:
        print(2)
        exit()

for a in squares:
    for b in squares:
        if N-a-b in squares:
            print(3)
            exit()

print(4)