A = int(input())
B = int(input())
C = int(input())

mul = A*B*C
arr = [0] * 10

for num in list(str(mul)):
    arr[int(num)] += 1 

print("\n".join(map(str, arr)))