# 백준 1620 나는야 포켓몬 마스터 이다솜

# 도감에 수록되어 잇는 포켓몬의 개수: N
# 내가 맞춰야 하는 문제의 개수: M

# N M 
# N개의 포켓몬 나열
# M개의 인풋 나열 

import sys
N, M = map(int, sys.stdin.readline().split())

d_names = {} # key: name value: num
d_keys = {} 

cnt = 1
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    d_names[name] = cnt
    d_keys[cnt] = name
    cnt += 1
    
for _ in range(M):
    word = sys.stdin.readline().rstrip()
    print("word:",word)
    
    if word.isdigit():
        print(d_keys[int(word)])
    else:
        print(d_names[word])