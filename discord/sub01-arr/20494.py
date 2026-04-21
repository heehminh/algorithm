# 26가지 A-Z
# N명, 의자/접시 N+1개

N = int(input())

ans = 0 
for _ in range(N):
    ans += len(input())

print(ans)