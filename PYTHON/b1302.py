# 백준 1302 베스트셀러 - 딕셔너리
import sys

input = sys.stdin.readline

N = int(input())
dict = {}
for _ in range(N):
    title = input()
    if title in dict.keys():
        dict[title] += 1
    else: 
        dict[title] = 1

for i in sorted(dict.keys()):
    if(dict[i] == max(dict.values())):
        print(i)
        break