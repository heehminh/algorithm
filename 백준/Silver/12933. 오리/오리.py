arr = input()
visited = [False] * len(arr)
ans = 0

if len(arr) % 5 != 0:
    print(-1)
    # break
    exit()


def solve(start):
    global ans
    prev = None
    k_cnt = 0
    q_cnt = 0
    for i in range(start, len(arr)):
        if not visited[i] and arr[i] == 'q' and q_cnt == 0:
            visited[i] = True
            prev = arr[i]
            q_cnt += 1
            continue
        elif not visited[i] and arr[i] == 'q' and prev == 'k':
            visited[i] = True
            prev = arr[i]
            continue

        if not visited[i] and arr[i] == 'u' and prev == 'q':
            visited[i] = True
            prev = arr[i]
            continue

        if not visited[i] and arr[i] == 'a' and prev == 'u':
            visited[i] = True
            prev = arr[i]
            continue

        if not visited[i] and arr[i] == 'c' and prev == 'a':
            visited[i] = True
            prev = arr[i]
            continue

        if not visited[i] and arr[i] == 'k' and prev == 'c' and k_cnt == 0:
            visited[i] = True
            prev = arr[i]
            ans += 1
            k_cnt += 1
            continue
        elif not visited[i] and arr[i] == 'k' and prev == 'c' and k_cnt > 0:
            visited[i] = True
            prev = arr[i]
            continue


for i in range(len(arr)):
    if arr[i] == 'q' and not visited[i]:
        solve(i)

if False in visited or ans == 0:
    print(-1)
else:
    print(ans)