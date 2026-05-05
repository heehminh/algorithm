def solution(msg):
    answer = [] 

    dict = {}
    for i in range(ord('Z')-ord('A')+1):
        dict[chr(i+65)] = i+1

    while msg:
        for i in range(len(msg), 0, -1):
            w = msg[:i]
            if w in dict:
                answer.append(dict[w])

                if i < len(msg) and w+msg[i] not in dict:
                    dict[w+msg[i]] = len(dict)+1

                msg = msg[i:]
                break
    
    return answer