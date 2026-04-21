# A의 앞, 뒤에 알파벳을 추가할 수 있다 
# A, B 길이 최대 50 (A의 길이는 B의 길이보다 작거나 같다, 같아질 때 까지 연산)

A, B = map(str, input().split())

def calculate(a, b):
    n = len(a)
    diff = 0
    
    for i in range(n):
        if a[i] != b[i]:
            diff += 1 

    return diff 

min_diff = 51
for i in range(len(B)-len(A)+1):
    min_diff = min(min_diff, calculate(A, B[i:i+len(A)]))
    
print(min_diff)

# A = koder, B = topcoder => 4번 비교
# 1. koder, (topco)der => diff: 4
# 2. koder, t(opcod)er => diff: 5 
# 3. koder, to(pcode)r => 5 
# 4. koder, top(coder) => 1 