def solution(today, terms, privacies):
    answer = []
    
    def to_day(date):
        year, month, day = map(int, date.split('.'))
        return year*12*28 + month*28 + day 
    
    today_to_date = to_day(today)
    
    # term dict 작업 
    term_dict = {}
    for k in range(len(terms)):
        name, date = terms[k].split()
        term_dict[name] = int(date) 
    
    for i in range(len(privacies)):
        first_date, term = privacies[i].split() # 2021.05.02, A
        due_date = to_day(first_date) + term_dict[term]*28 - 1

        if due_date < today_to_date: 
            answer.append(i+1) 
        
    return answer