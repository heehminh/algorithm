T = int(input())

for _ in range(T):
    N = int(input())
    dict = {}
    ans = 1

    for _ in range(N):
        name, type = map(str, input().split())
        dict[name] = type 
    
    unique_type = set(dict.values())
    
    for type in unique_type:
        cnt = list(dict.values()).count(type)
        ans *= (cnt+1)
    
    print(ans-1)
    # 종류별로+1 씩 모두 곱한뒤 -1 (알몸)