from copy import deepcopy  
  
T = int(input())  
for tc in range(T):  
    N, rotate = map(int, input().split())  
    arr = [list(map(int, input().split())) for _ in range(N)]  
    # 결과 저장할 배열  
    result = [[0]*N for _ in range(N)]  
  
    if rotate < 0:  
        rotate = 360 + rotate  
    # 제자리 일 경우 그대로 출력  
    if rotate == 360 or rotate == 0:  
        for l in arr:  
            print(*l)  
    else:  
        # 45의 배수로 나오므로 나눈 몫만큼 반복해주어야 한다.  
        for _ in range(rotate//45):  
            for i in range(N):  
                for j in range(N):  
                    # 주 대각선이라면 가운데 행을 들고 와준다.  
                    if i==j:  
                        result[i][j] = arr[N//2][j]  
                    # 가운데 행이라면 부 대각선을 들고와준다.  
                    elif i == N//2:  
                        result[i][j] = arr[N-j-1][j]  
                    # 부 대각선이라면 가운데 열을 들고온다  
                    # 부 대각선 좌표 방법 2가지                    
                    # i+j = N-1                    
                    # N-j-1 = i                    
                    elif i+j == N-1:  
                        result[i][j] = arr[i][N//2]  
                    # 가운데 열이라면 주 대각선을 들고온다.  
                    elif j == N//2:  
                        result[i][j] = arr[i][i]  
  
                    # 모두 아니라면 같은 좌표값 들고오기  
                    else:  
                        result[i][j] = arr[i][j]  
            # 회전을 더해야할수도 있으므로 복사해주기  
            arr = deepcopy(result)  
  
        for k in result:  
            print(*k)  