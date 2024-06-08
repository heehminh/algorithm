N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
result = []

if (N%2 == 0):
    # 짝수 
    j = N-1
    
else:
    # 홀수 
    j = N-2
    result.append(arr[-1])

i = 0 
while i<j:
    cnt = arr[i]+arr[j]
    result.append(cnt)
    
    i+=1
    j-=1

print(max(result))
