def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    ext_num = dict[ext]
    sort_num = dict[sort_by]
    
    for item in data:
        if item[ext_num] < val_ext:
            answer.append(item)
            
    answer.sort(key=lambda x:x[sort_num])
    
    return answer