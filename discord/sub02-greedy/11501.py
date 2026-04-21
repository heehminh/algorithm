# 1. 주식 하나를 산다.
# 2. 원하는 만큼 가지고 있는 주식을 판다.
# 3. 아무것도 안한다

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    reverse_arr = arr[::-1] 
    
    max_price = reverse_arr[0]
    ans = 0
    
    for i in range(N):
        if max_price < reverse_arr[i]:
            max_price = reverse_arr[i]
        else:
            ans += (max_price - reverse_arr[i])
    
    print(ans)