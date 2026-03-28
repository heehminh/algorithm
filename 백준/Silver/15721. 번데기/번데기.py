A = int(input())
T = int(input())
N = int(input())

games = [] # 게임 진행 상황 (튜플로 저장)
bbun = 1 # 뻔 을 외친 횟수
degi = 1 # 데기 를 외친 횟수
cnt = 0 # 몇번째 게임인지 

while(True):
    num = bbun # 이전 회차에서 뻔 or 데기를 외친 누적 횟수
    cnt += 1
    
    games.append((bbun, 0))
    games.append((degi, 1))
    bbun += 1
    degi += 1
    games.append((bbun, 0))
    games.append((degi, 1))
    bbun += 1
    degi += 1
    
    # (1): 뻔 - 뻔 - (2): 뻔 - 뻔 - 뻔 (N): N+1번 
    for _ in range(cnt + 1):
        games.append((bbun, 0))
        bbun += 1
    
    # 데기 - 데기
    for _ in range(cnt + 1):
        games.append((degi, 1))
        degi += 1 
        
    if num < T <= bbun:
        print(games.index((T, N)) % A)
        break
     
