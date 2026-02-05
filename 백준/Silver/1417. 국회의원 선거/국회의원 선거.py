N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 0

while True:
    if N == 1:
        break
    
    # 후보 중 최댓값
    max_num = max(arr[1:])
    
    if arr[0] > max_num:
        break
    
    # 최댓값을 가진 후보의 인덱스 
    idx = arr[1:].index(max_num)+1
    arr[0] += 1 
    arr[idx] -= 1 
    ans += 1 

print(ans)