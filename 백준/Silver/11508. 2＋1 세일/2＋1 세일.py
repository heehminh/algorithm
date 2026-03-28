# 백준 11508 2+1 세일
# 그중에서 싼 것은 무료로 지불하고 나머지 두개의 제품 가격만 지불 
# 할인되는게 비쌀수록 좋음 (가장 비싼것끼리 3개씩 묶어놓기)
# 3 3 [2] 2 -> 8
# 6 5 [5] 5 5 [4] -> 21 
# i%3 == 2 인 경우를 제외해주기

import sys
import math
N = int(sys.stdin.readline())
carts = [int(input()) for _ in range(N)]
carts.sort()
carts.reverse()

ans = sum(carts)
for i in range(2, N, 3):
    ans -= carts[i]
    
print(ans)



