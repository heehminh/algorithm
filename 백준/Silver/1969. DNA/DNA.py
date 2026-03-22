import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
arr.sort()

ans = 0 
dna = ''

for i in range(M):
    a, t, g, c = 0, 0, 0, 0
    
    for j in range(N):
        if arr[j][i] == 'A':
            a += 1 
        elif arr[j][i] == 'T':
            t += 1 
        elif arr[j][i] == 'G':
            g += 1 
        elif arr[j][i] == 'C':
            c += 1 
    
    max_dna = max(a, t, g, c)
    sum = a+c+g+t
    # 사전순: A > C > G > T 
    if max_dna == a:
        dna += 'A'
        ans += sum-a
    elif max_dna == c:
        dna += 'C'
        ans += sum-c
    elif max_dna == g:
        dna += 'G'
        ans += sum-g
    elif max_dna == t:
        dna += 'T'
        ans += sum-t 

print(dna)
print(ans)