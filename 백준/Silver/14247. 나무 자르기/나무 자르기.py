# 백준 14247 나무자르기

# 성장속도가 제일 더딘 나무부터 빠른 나무순으로 정렬 후 베면 된다
# 나무를 1번씩만 베는 것이 최적 
import sys 

N = int(sys.stdin.readline())

heights = list(map(int, sys.stdin.readline().split()))
speeds = list(map(int, sys.stdin.readline().split()))

arr = []
for i in range(N):
    arr.append([speeds[i],heights[i]])

arr.sort()

ans = 0
# for i in range(N):
#     ans += arr[i][1]
#     for j in range(N):
#         arr[j][1] += arr[j][0] -> 시간초과

for i in range(N):
    ans += arr[i][0]*i + arr[i][1]
    # 1*0 + 6
    # 2*1 + 1
    # 3*2 + 2
    # 4*3 + 4
    # 7*4 + 3
    
print(ans)

