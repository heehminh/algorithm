# 백준 2748 피보나치 수2

cache = [-1] * 91 
cache[0] = 0
cache[1] = 1 

# 방법 1) Top-down: 재귀 
def f(n):
    if cache[n] == -1: # n번째 피보나치 수열을 처음으로 구하면
        cache[n] = f(n-2) + f(n-1)
        
    return cache[n]
        
print(f(int(input())))

# 방법 2) Bottom-up: 반복문 
N = int(input())

for i in range(2, N+1):
    cache[i] = cache[i-1] + cache[i-2]
print(cache[N])

# 시간초과
# def fib(n):
#     if n == 0 or n==1 : 
#         return n
#     else: 
#         return fib(n-2) + fib(n-1)

# print(fib(n)) 

