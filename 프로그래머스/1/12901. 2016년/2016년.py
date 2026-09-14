def solution(a, b):
    answer = ''
    
    arr = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    dates = [0, 31]
    
    for i in range(2, 12+1):
        if i == 2:
            month = 29 
        elif i in (4, 6, 9, 11):
            month = 30 
        else:
            month = 31 
        
        dates.append(dates[-1] + month)
        
    today = dates[a-1] + b 
    return arr[today % 7]