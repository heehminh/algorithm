X = int(input())
ans = False

for i in range(1000000):
    if sorted(list(str(X))) == sorted(list(str(i))) and i > X:
        print(i)
        ans = True 
        break 

if ans == False:
    print(0)