total_expect = int(input())
cnt = int(input()) 

result = 0

for i in range(cnt):
    price, count = input().split()
    price = int(price)
    count = int(count)
    
    result += price*count
    
if (result == total_expect): 
    print("Yes")
else:
    print("No")