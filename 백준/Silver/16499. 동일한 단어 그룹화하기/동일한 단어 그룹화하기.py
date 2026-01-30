N = int(input())
arr = []

for _ in range(N):
    word_list = list(input())
    if sorted(word_list) not in arr:
        arr.append(sorted(word_list))

print(len(arr))