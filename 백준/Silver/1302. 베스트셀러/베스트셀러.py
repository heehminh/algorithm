# 오늘 하루 동안 팔린 책의 제목 -> 가장 많이 팔린 책의 제목
# 가장 많이 팔린 책이 여러 개일 경우엔 사전 순으로 가장 앞서는 제목

import sys 
N = int(sys.stdin.readline())

m = {}
for _ in range(N):
    title = sys.stdin.readline()
    if (title in m.keys()):
        m[title] += 1 
    else:
        m[title] = 1

for i in sorted(m.keys()):
    if (m[i] == max(m.values())): 
        print(i)
        break
    