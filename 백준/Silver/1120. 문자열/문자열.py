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