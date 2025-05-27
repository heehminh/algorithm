import sys 

N, M = map(int, input().split())

name_key = {}
idx_key = {}

for i in range(N): # N 100,000 이하 
    name = sys.stdin.readline().strip()
    name_key[name] = i+1 
    idx_key[i+1] = name  
    
for _ in range(M): # M 100,000 이하 
    q = sys.stdin.readline().strip()
    
    if q.isdigit():
        # 포켓몬 이름 출력
        print(idx_key[int(q)])
    else:
        # 포켓몬 번호 출력 
        print(name_key[q])