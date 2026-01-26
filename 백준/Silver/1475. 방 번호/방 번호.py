N = int(input())
ans = 1

arr = [i for i in range(10)]

for i in list(str(N)):
    if int(i) in arr:
        arr.remove(int(i))
        
    # 6, 9 처리 
    elif int(i) == 6 and 9 in arr: 
        arr.remove(9)
        
    elif int(i) == 9 and 6 in arr:
        arr.remove(6) 
        
    else:
        ans += 1 
        arr.extend([i for i in range(10)])
        arr.remove(int(i))

print(ans)