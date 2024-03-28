# 평균
N = int(input())
originals = list(map(int, input().split()))
maxNum = max(originals)
new = []

for i in range(N):
    new.append(originals[i]/maxNum*100)

print(sum(new) / len(new))
