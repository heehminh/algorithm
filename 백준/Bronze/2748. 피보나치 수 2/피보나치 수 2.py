cache = [-1] * 91 
cache[0] = 0
cache[1] = 1 

# top-down: 메모이제이션 
def f(n):
    if cache[n] == -1: # n번째 피보나치 수열을 처음으로 구하면
        cache[n] = f(n-2) + f(n-1)
        
    return cache[n]
        
print(f(int(input())))