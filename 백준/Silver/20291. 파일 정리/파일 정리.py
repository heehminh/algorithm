N = int(input())

file_dict = {}

for _ in range(N):
    name, extend = map(str, input().split('.'))
    
    if extend in file_dict.keys():
        file_dict[extend] += 1 
    else:
        file_dict[extend] = 1 

for k, v in sorted(file_dict.items()):
    print(k, v)