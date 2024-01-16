def solution(data):
    sList = data[0] # 종배열 
    cList = data[1] # 수배열 
    dict = {}
    
    for i in range(len(sList)):
        if sList[i] in dict:
            dict[sList[i]] += cList[i]
        else:
            dict[sList[i]] = cList[i]
    
    # 1) value를 기준으로 오름차순 정렬 2) key를 기준으로 오름차순 정렬 
    dict = sorted(dict.items(), key=lambda item: (-item[1], item[0]))

    # keys만 출력 
    keys = [i[0] for i in dict]
    
    return keys