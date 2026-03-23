import sys 
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

def is_same(a, b):
    if len(a) != len(b):
        return False 
    return a in (b+b) # ture'picture'pic

result = []

for w in words:
    found = False 
    
    for r in result:
        if is_same(w, r):
            found = True 
            break 
    
    if not found: 
        result.append(w)
    
print(len(result))