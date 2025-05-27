# 1대: 1분에 한대당 A원 / 2대 / 3대 

a, b, c = map(int, input().split())

arr = [0]*100

for _ in range(3):
    x, y = map(int, input().split())
    for i in range(x, y):
        arr[i] += 1 
        
ans = 0 
for num in arr:    
    if num == 1:
        ans += a 
    elif num == 2:
        ans += b*2 
    elif num == 3:
        ans += c*3

print(ans)
