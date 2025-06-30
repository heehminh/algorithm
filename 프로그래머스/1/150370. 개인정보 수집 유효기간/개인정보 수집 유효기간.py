def solution(today, terms, privacies):
    answer = []
    
    today_year, today_month, today_day = map(int, today.split('.'))
    today_to_date = today_year*12*28 + today_month*28 + today_day
    
    # term dict 작업 
    term_dict = {}
    for k in range(len(terms)):
        name, date = terms[k].split()
        term_dict[name] = int(date) 
    
    for i in range(len(privacies)):
        first_date, term = privacies[i].split() # 2021.05.02, A
        year, month, day = map(int, first_date.split('.')) # 2021, 5, 2 
        due_date = year*12*28 + month*28 + day + term_dict[term]*28 - 1 

        if due_date < today_to_date: # 날짜 비교
            answer.append(i+1) 
        
    return answer