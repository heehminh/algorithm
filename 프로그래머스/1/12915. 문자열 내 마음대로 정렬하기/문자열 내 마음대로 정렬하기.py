def solution(strings, n):
    answer = []
    wList = []
    
    for idx in range(len(strings)):
        tmp = []
        tmp.append(strings[idx])
        tmp.append(list(strings[idx]))
        wList.append(tmp)
    
    wList.sort(key=lambda x: (x[1][n], x[0]))
    
    for w in wList:
        answer.append(w[0])
    
    return answer