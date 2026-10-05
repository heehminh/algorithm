def find_bottom(si, sj, ei, ej):
    # 행의 합이 0이면 내려감 
    for i in range(ei, N+1):
        if sum(arr[i][sj:ej]) != 0:
            return i 
    
    return N+1 

def mark(num, si, sj, ei, ej):
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = num 

def drop(num):
    si, sj, ei, ej = unit[num]

    bottom_idx = find_bottom(si, sj, ei, ej) # 바닥 좌표 함수 
    nxt_si, nxt_ei = bottom_idx-(ei-si), bottom_idx 

    mark(0, si, sj, ei, ej)
    mark(num, nxt_si, sj, nxt_ei, ej)

    unit[num] = [nxt_si, sj, nxt_ei, ej]

    
# 위로 올라가면서 만나는 박스 중력처리, 아래로 내림 
def gravity(si, sj, ei, ej):
    sset = set() # 중복처리 

    for i in range(si-1, 0, -1):
        for j in range(1, N+1):
            if arr[i][j] != 0 and arr[i][j] not in sset:
                drop(arr[i][j]) # 박스번호
                sset.add(arr[i][j])


################################################

N, M = map(int, input().split())

arr = [[0] * (N+1) for _ in range(N+1)]
unit = {}
chk = [0] * 101 # 존재하는 박스 
answer = []

for _ in range(M):
    k, h, w, c = map(int, input().split())
    
    si, sj, ei, ej = 1, c, 1+h, c+w

    bottom_idx = find_bottom(si, sj, ei, ej) # 바닥 좌표 함수 
    nxt_si, nxt_ei = bottom_idx-h, bottom_idx 

    mark(k, nxt_si, sj, nxt_ei, ej) # 번호 표시 함수 

    unit[k] = [nxt_si, sj, nxt_ei, ej]
    chk[k] = 1 

# [2] 택배하차
# 좌우 반복처리, 번호순, 뺀 후 중력처리
# M개 박스: 오름차순으로 존재하는 박스 중 왼쪽/오른쪽 삭제 후 
left = True 
for _ in range(M):
    for num in range(1, 101):
        if chk[num] == 0:
            continue 
        
        si, sj, ei, ej = unit[num]
        
        for i in range(si, ei):
            if left: # 왼쪽 
                if sum(arr[i][1:sj]) != 0:
                    break 
            else: # 오른쪽
                if sum(arr[i][ej:N+1]) != 0:
                    break 

        else:
            chk[num] = 0 
            mark(0, si, sj, ei, ej)
            answer.append(num)

            # 중력처리 
            gravity(si, sj, ei, ej)
            left = not left 
            break  


for a in answer:
    print(a)