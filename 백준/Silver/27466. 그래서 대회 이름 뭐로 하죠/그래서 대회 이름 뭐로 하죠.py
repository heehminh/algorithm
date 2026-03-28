import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
str = list(input().rstrip())

def is_fail(idx):
    if idx == -1:
        print('NO')
        exit()
    
# 1) 맨 뒤 (AEIOU가 아님)
idx1 = -1 
for i in range(N-1, -1, -1):
    if str[i] not in 'AEIOU':
        idx1 = i 
        break 

is_fail(idx1)

# 2) 뒤에서 2, 3번째 (A임)
idx2 = -1 
for i in range(idx1-1, -1, -1):
    if str[i] == 'A':
        idx2 = i 
        break 

is_fail(idx2)

idx3 = -1
for i in range(idx2-1, -1, -1):
    if str[i] == 'A':
        idx3 = i 
        break 

is_fail(idx3)

# 3) 앞에서 M-3개 채워야함
if idx3 < M-3:
    print('NO')
else:
    print('YES')
    print(''.join(str[:M-3]) + 'AA' + str[idx1])