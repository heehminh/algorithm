X = int(input())

for i in range(1000000):
    if sorted(list(str(X))) == sorted(list(str(i))) and i > X:
        print(i)
        exit()

print(0)