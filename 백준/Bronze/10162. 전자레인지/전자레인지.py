T = int(input())
arr = [300, 60, 10]

ans = []

for i in range(3):
    ans.append(int(T/arr[i]))
    T %= arr[i]

if T > 0:
    print(-1)
else: 
    print(" ".join(map(str, ans)))