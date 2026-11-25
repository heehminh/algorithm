def solution(n):
    answer = 0

    for i in range(len(str(n))):
        answer += int(list(str(n))[i])

    return answer