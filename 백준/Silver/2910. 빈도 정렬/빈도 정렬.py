import sys 
N, C = map(int, sys.stdin.readline().split())

m = {}
testCase = list(map(int, sys.stdin.readline().split(" ")))

for i in testCase:
    if (i in m.keys()):
        m[i] += 1
    else:
        m[i] = 1

keys = list(m.keys())
keys.sort(key=lambda x:m[x], reverse=True)

ans = []
for key in keys:
    for i in range(m[key]):
        ans.append(str(key))
print(" ".join(ans))