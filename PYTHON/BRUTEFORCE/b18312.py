# 백준 18312 시각 
# 00시 00분 00초 ~ N시 59분 59초 
N, K = map(int, input().split())

result = 0
for i in range(N+1):
    str_list = []
    
    if i < 10:
        i = '0' + str(i)
          
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        
        for k in range(60):
            if k < 10:
                k = '0' + str(k)
            
            str_list = str(i)+str(j)+str(k) # 50833
            if str(K) in str_list:
                result += 1

print(result)