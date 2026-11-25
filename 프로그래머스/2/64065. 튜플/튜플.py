def solution(s):
    answer = []
    cnt_dict = {}
    
    # 1. {} 을 기준으로 나누기 
    # 2. 원소의 개수 세기
    
    num = ''
    for t in s:
        if t != '{' and t != '}' and t != ',':
            num += t 
            
        elif num != '':
            num = int(num)
            
            if num in cnt_dict.keys():
                cnt_dict[num] += 1 
            else:
                cnt_dict[num] = 1 
            
            num = ''
    
    # 3. 많은 순서대로 앞으로 배정 
    sorted_cnt_dict = sorted(cnt_dict.items(), key = lambda x: x[1], reverse=True)
    
    for k, v in sorted_cnt_dict:
        answer.append(k)
    
    return answer