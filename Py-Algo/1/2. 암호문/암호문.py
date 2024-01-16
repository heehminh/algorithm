def solution(data):
    import re 
    result = 0 
    
    p = re.findall('([rev])(10|[0-9])', data)
    for k, v in p:
        result += int(v) 
    
    return f"{result//10}월 {result%10}일"