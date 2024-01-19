def solution(data):
    cnt = int(len(data)*0.3) # 선발해야 하는 인원
    if cnt == 0:
        return []
    
    pick = 0 # 선발된 인원
    dict = {} # 점수 딕셔너리 
    result = []
    
    for i in data:
        if sum(i[1:]) in dict:
            dict[sum(i[1:])] += i[0]
        else: 
            dict[sum(i[1:])] = i[0]
            
    for i in sorted(list(dict.items()), key=lambda x: x[0], reverse=True):
        if pick < cnt and len(i[1]) <= cnt:
            result.extend(i[1])
            pick += len(i[1])
        elif len(i[1]) > cnt:
            return result 
        
    return sorted(result, reverse=True)  