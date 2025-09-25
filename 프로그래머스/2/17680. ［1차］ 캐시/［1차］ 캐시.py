def solution(cacheSize, cities):
    answer = 0
    
    dict = {} 
    cnt = 0 
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        if city.lower() in dict:
            dict[city.lower()] = cnt 
            answer += 1 
        
        elif len(dict) < cacheSize:
            dict[city.lower()] = cnt 
            answer += 5 
        
        else:
            # 숫자가 젤 작은거 삭제
            k = min(dict, key=dict.get)
            del dict[k]
            dict[city.lower()] = cnt 
            answer += 5

        cnt += 1 
            
    
    return answer