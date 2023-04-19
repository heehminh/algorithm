# 패션왕 신해빈 

# 테스트 케이스 
# n: 해빈이가 가진 의상의 수 
# 의상의 이름, 의상의 종류 

testCase = int(input())
for _ in range(testCase):
    n = int(input())
    
    m = {}
    for i in range(n):
        ans = n
        costume = list(map(str, input().split()))
        if (costume[1] in m.keys()):
            m[costume[1]] += 1 
        else:
            m[costume[1]] = 2
    
    ans = 1 
    for i in m.values():
        ans *= i 
    print(ans-1)
        
        
        
        