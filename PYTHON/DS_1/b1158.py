# 백준 1158 요세푸스 문제 
N, K = map(int, input().split())

arr = []
for i in range(1, N+1):
    arr.append(i)
    
result = []
target = 0 

for _ in range(N):
    target += K-1
    if target >= len(arr):
        target = target%len(arr)
    result.append(str(arr.pop(target)))

print("<",", ".join(result)[:],">", sep='')