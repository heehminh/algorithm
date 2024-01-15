def solution(data):
    result = 0
    cnt = data // 3300
    charge = data - 3300*cnt
    result += cnt + min(cnt // 10, charge // 300) 
    
    return result