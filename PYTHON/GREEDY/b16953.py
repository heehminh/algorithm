# 백준 16953 A->B
# 2 162 (필요한 연산의 최솟값 찾기)

A, B = map(int, input().split())

cnt = 0

while (A < B):
    if B%10 == 1:
        B = int(B/10)
        cnt += 1
    else:
        if B%2 == 0:
            B = int(B/2)
            cnt += 1 
        else:
            break

print(cnt+1 if A==B else -1)