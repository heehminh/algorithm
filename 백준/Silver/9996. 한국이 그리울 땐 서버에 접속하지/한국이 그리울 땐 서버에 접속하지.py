import re 

N = int(input())
p_ = list(input())
p = ''

for i in range(len(p_)):
    if p_[i] == '*':
        p += '[a-z]*' # 빈 문자열도 가능 
    else:
        p += p_[i]

arr = [input() for _ in range(N)]

for str in arr:
    ans = re.search(p, str) 
    if ans and ans.start() == 0 and ans.end() == len(str):
        print('DA')
    else: 
        print('NE')