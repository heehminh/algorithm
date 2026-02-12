N, A, B = map(int, input().split())
arr_2x1 = list(map(int, input().split()))
arr_2x2 = list(map(int, input().split()))

arr_2x1.sort()
arr_2x2.sort()

ans = 0

if N % 2 == 1:
    ans += arr_2x1.pop()
    N -= 1

for _ in range(N//2):
    if len(arr_2x1) < 2:
        ans += arr_2x2.pop()
        continue

    pair = arr_2x1[-1] + arr_2x1[-2]

    if len(arr_2x2) < 1:
        ans += pair
        arr_2x1.pop()
        arr_2x1.pop()
        continue
    
    if arr_2x2[-1] > pair:
        ans += arr_2x2.pop()
    
    else:
        ans += pair
        arr_2x1.pop()
        arr_2x1.pop()

print(ans)