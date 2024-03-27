# 두가지 경우 
# 1번 - 행+열의 합이 짝수이면 W/ 홀수이면 B (1-8로 가정)
# 2번 - 반대의 경우 ) 둘 다 구해서 min() 
# N, M: 8~50 -> 모든 경우 탐색

N, M = map(int, input().split())
board=[]
ans=[]

for i in range(N):
    board.append(input())
    
for a in range(N-7):
    for b in range(M-7):
        idx1, idx2 = 0, 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] == 'B':
                        idx1 += 1
                    if board[i][j] == 'W':
                        idx2 += 1 
                else:
                    if board[i][j] == 'W':
                        idx1 += 1
                    if board[i][j] == 'B':
                        idx2 += 1 
        ans.append(min(idx1, idx2))

print(min(ans))