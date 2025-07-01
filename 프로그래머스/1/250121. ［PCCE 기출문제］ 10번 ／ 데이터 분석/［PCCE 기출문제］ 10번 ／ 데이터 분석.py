def name_to_num(name):
    num = 0 
    if name == 'date':
        num = 1 
    elif name == 'maximum':
        num = 2 
    elif name == 'remain':
        num = 3 

    return num 

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    ext_num = name_to_num(ext)
    sort_num = name_to_num(sort_by)
    
    for item in data:
        if item[ext_num] < val_ext:
            answer.append(item)
            
    answer.sort(key=lambda x:x[sort_num])
    
    return answer