N = int(input())
cache = [0] * 1001

cache[1] = 1
cache[2] = 2 

def dp(n):
    if cache[n] > 0:
        return cache[n]

    cache[n] = dp(n-1) + dp(n-2)
    cache[n] %= 10007
    
    return cache[n]

print(dp(N))