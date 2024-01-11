# 백준 13305 주유소
# 그 다음 주유소의 값이 더 싸다면 필요한만큼만 넣기
# 도로의 길이
# 주유소의 리터당 가격 

# 예제 1) 
#   2   3   1
# 5   2   4   1
# 5*2 + 2*(3+1) = 10+8 = 18 (더 작은걸만나기 전까지)

# 예제 2)
#   3   3   4
# 1   1   1   1
# 1*(3+3+4) = 10

import sys

N = int(sys.stdin.readline())
citys = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

ans = 0 # 비용
min = prices[0]
for i in range(N-1):
    if min > prices[i]:
        min = prices[i]
             
    ans += min*citys[i]
    
print(ans)