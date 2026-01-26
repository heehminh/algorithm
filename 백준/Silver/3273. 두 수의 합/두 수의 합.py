from itertools import combinations
import sys 

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()

ans = 0
start = 0
end = N-1 # 투포인터 

while start < end:
    num = arr[start] + arr[end]
    
    if num == X:
        ans += 1
        start += 1 

    elif num < X:
        start += 1 
    else:
        end -= 1
        
print(ans)