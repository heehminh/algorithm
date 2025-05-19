T = int(input()) # 학기

for _ in range(T):
    N = int(input()) # 들은 과목 
    total_c = 0 
    total_g = 0 
    
    for _ in range(N):
        C, G = input().split()
        total_c += int(C) 
        total_g += int(C)*float(G)
    
    print(total_c, round(total_g/total_c, 1))