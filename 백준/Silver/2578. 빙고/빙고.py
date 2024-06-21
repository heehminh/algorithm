# 백준 빙고 
myBingo = [list(map(int, input().split())) for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]

# 몇번째 수 
res = 0 
bingo_flag = False

# 빙고 콜을 할 때 숫자 0으로 대체 
def make_zero(num):
    for i in range(5):
        for j in range(5):
            if myBingo[i][j] == num:
                myBingo[i][j] = 0
                return 

# 빙고의 수 체크 
def is_bingo():
    ans = 0 
    
    for i in range(5):
        # 가로 
        if myBingo[i][0]==0 and myBingo[i][1]==0 and myBingo[i][2]==0 and myBingo[i][3]==0 and myBingo[i][4]==0:
            ans += 1 
        # 세로 
        if myBingo[0][i]==0 and myBingo[1][i]==0 and myBingo[2][i]==0 and myBingo[3][i]==0 and myBingo[4][i]==0:
            ans += 1 
    
    # 대각선
    if myBingo[0][0]==0 and myBingo[1][1]==0 and myBingo[2][2]==0 and myBingo[3][3]==0 and myBingo[4][4]==0:
        ans += 1 
    if myBingo[0][4]==0 and myBingo[1][3]==0 and myBingo[2][2]==0 and myBingo[3][1]==0 and myBingo[4][0]==0:
        ans += 1 
    
    return ans 

for i in calls:
    if bingo_flag: ## bingo_flag를 추가하지않으면 빙고가 3개이상되었을 때, 3개가 모두 출력됨
        break 
    
    for j in i:
        make_zero(j) 
        res += 1 
        
        if is_bingo() >= 3:
            print(res)
            bingo_flag = True 
            break