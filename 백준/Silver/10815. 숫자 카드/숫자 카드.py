# 백준 10812 숫자 카드 => 시간초과 
import sys 
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort() # 이분 탐색 

M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

ans = []
for m in m_list:
    l = bisect_left(n_list, m)
    r = bisect_right(n_list, m)
    ans.append(1 if r-l>0 else 0)
    # ans.append(1 if n_list[l]==m else 0)

print(*ans)

# 시간 초과
# for m in m_list:
#    print(1 if (m in n_list) else 0, end =" ")