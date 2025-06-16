# combinations 안쓰고 풀기 
arr = [int(input()) for _ in range(9)]
arr.sort()

for i in range(8): 
    for j in range(i+1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(arr[k])
            exit()