# 백준 1931 회의실 배정
# 종료 시간이 가장 이른순으로 배정
# 시작하는 시간의 오름차순

import sys
N = int(sys.stdin.readline())
rooms = []
for _ in range(N):
    room = list(map(int, sys.stdin.readline().split()))
    rooms.append(room)
    
rooms.sort(key = lambda x: (x[1], x[0]))
# 종료시간이 가장 이른순으로 배정
# 종료시간이 같은 경우엔 시작하는 시간이 빠른 순으로 배정
# why? 회의의 시작시간과 끝나는 시간이 같을 수 있다
# (1, 2) (2, 2) 인 경우 다음과 같이 sort 해야 둘 다 배정가능 
    
finish = 0
ans = 0
for room in rooms:
   if finish <= room[0]:
       # 종료 시간이 가장 이른 회의 배정해준후
       # 그 회의의 종료 시간으로 시작 시간을 바꿔줌
        finish = room[1]
        ans += 1

print(ans)