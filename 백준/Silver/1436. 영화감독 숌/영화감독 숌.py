# 종말의 수: 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
# N~10000 (세다가 N에 도달하면 끝)

N = int(input())
ans = 666 # N번째 종말의 수로 업데이트 
cnt = 0 # 몇번째인지

while(True):
    if '666' in str(ans):
        cnt += 1
    
    if cnt == N:
        break 

    ans += 1

print(ans)