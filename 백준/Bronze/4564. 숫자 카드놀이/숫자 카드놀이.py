def mul(num):
    res = [num]
    while num >= 10:
        temp = 1 
        for i in str(num):
            temp *= int(i)
        res.append(temp)
        num = temp 
    return res 

while True:
    S = int(input())
    if S == 0: 
        break 
    
    print(*mul(S))

