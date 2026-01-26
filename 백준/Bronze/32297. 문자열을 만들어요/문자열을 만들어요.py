N = int(input())
string = input()

ans = False 

for i in range(N-3):
    if string[i:i+4] == 'gori':
        ans = True 
        
print('YES') if ans else print('NO') 