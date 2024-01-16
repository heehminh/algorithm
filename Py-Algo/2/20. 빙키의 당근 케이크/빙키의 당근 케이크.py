def solution(data):
    names = data[0][0]
    prices = data[0][1]
    priors = data[0][2] # -> dict로 만들어서 key에 index를 주기 
    budget = data[1]
    
    result = []
    prior_dict = {}
    
    for i in range(len(priors)):
        prior_dict[i] = priors[i] # {0: 4}
        
    # prior_dict을 value를 기준으로 오름차순 정렬 
    prior_dict = sorted(prior_dict.items(), key=lambda item: item[1])
    
    for k,v in prior_dict:
        budget -= prices[k]
        if (budget >= 0):
            result.append(names[k])
       
    return result