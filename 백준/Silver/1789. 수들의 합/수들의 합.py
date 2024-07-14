# 수들의 합
# 서로 다른 N개의 자연수의 합이 S 
# 자연수 N의 최댓값

S = int(input())
rest = S # S - 2i 의 잔여값 
ans = 0

for i in range(1, S+1):
    if rest >= i:
        rest -= i 
        ans += 1 
    else: # 시간초과 
        break

print(ans)