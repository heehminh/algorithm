num = 1000 - int(input())
arr = [500, 100, 50, 10, 5, 1]
ans = 0 

i = 0 
while num >= arr[-1]:
    if num / arr[i] > 0:
        ans += num//arr[i]
        num = num%arr[i]
    
    i += 1 

print(ans)