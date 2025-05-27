N = int(input())
arr = [input() for _ in range(N)]

names = {}

for i in range(N):
    if arr[i][:1] not in names.keys():
        names[arr[i][:1]] = 1 
    else:
        names[arr[i][:1]] += 1 

ans = ''
for name in sorted(names.keys()):
    if names[name] >= 5:
        ans += name

if ans == '':
    print('PREDAJA')
else:
    print(ans)