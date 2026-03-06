import sys
input = sys.stdin.readline 

left, right = map(str, input().split())

keyboards = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

# 한글에서 모음 목록
vowels = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']

targets = list(input().rstrip())

def find_idx(s):
    for y in range(3):
        for x in range(len(keyboards[y])):
            if keyboards[y][x] == s:
                return [y, x]

before_left_idx = find_idx(left)
before_right_idx = find_idx(right)

ans = 0 

for t in targets:
    idx = find_idx(t)
    
    if t in vowels:
        ans += (abs(idx[0]-before_right_idx[0]) + abs(idx[1]-before_right_idx[1]))
        before_right_idx = idx  
    else:
        ans += (abs(idx[0]-before_left_idx[0]) + abs(idx[1]-before_left_idx[1]))
        before_left_idx = idx 
    
    ans += 1 # 누르는 시간 

print(ans)