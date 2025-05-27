# N: 온도를 측정한 전체 날짜의 수 
# K: 합을 구하기 위한 연속적인 날짜 
# 합이 최대가 되는 값

import sys 

N, K = map(int, input().split())
arr = list(map(int, input().split()))

psum = [0] * (N+1)
max_sum = (N+1) * -100 

# 누적합
for i in range(N):
    psum[i+1] += psum[i] + arr[i]

# 구간합 
for i in range(N-K+1):
    temp_sum = psum[i+K] - psum[i]
    max_sum = max(temp_sum, max_sum)
    
print(max_sum)