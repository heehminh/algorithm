import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
arr.sort()

ans = 0 
dna = ''

for i in range(M):
    # 1. 가장 많이 나온 문자 
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
    
    # 2. 가장 많이 나온 문자를 DNA에 저장 
    max_dna = max(a, t, g, c)
    sum = a+c+g+t
    # 사전순: A > C > G > T 
    if max_dna == a:
        dna += 'A'
        ans += sum-a # 3. 가장 많이 나온 문자를 제외한 문자
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