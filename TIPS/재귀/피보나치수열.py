# 1. 일반 함수 - 시간복잡도 O(n), 공간복잡도 O(1)
def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1 
    for _ in range(1, n):
        a, b = b, a+b
    
    return a

print([fib(x) for x in range(1, 10)])

# 2. 재귀 - 시간복잡도 O(2^n), 공간복잡도 O(n)
def fib2(n):
    if n==1 or n==2:
        return 1 
    else:
        return fib2(n-1) + fib2(n-2)
    
print([fib2(x) for x in range(1, 10)])

# 3. 메모이제이션 - 시간복잡도 O(n), 공간복잡도 O(n)
def fib3(n):
    fibList = [1, 1]
    if n==1 or n==2:
        return 1 
    for i in range(2, n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList

print(fib3(9))