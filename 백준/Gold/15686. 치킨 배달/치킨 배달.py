# 0: 빈칸 1: 집 2: 치킨집 
# 1~5 
# 도시의 치킨거리가 가장 작게 
from itertools import combinations

N, M = map(int, input().split())
board = [input().split(" ") for _ in range(N)]

chicken = [] # [1,2], [2,2], [4,4]

# 치킨집의 개수가 M인 경우 -> 최소거리만 출력
# N^2: 2500 
for i in range(N):
    for j in range(N):
        if board[i][j] == '2':
            chicken.append([i,j])

ans = 100000 

# 13C6최대 * N^2 * 6
for chick in combinations(chicken, M):
    tmp_ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '1':
                min_dis = 1000
                for c1, c2 in chick:
                    min_dis = min(min_dis, abs(c1-i)+abs(c2-j))
                tmp_ans += min_dis
    ans = min(ans, tmp_ans)

print(ans)