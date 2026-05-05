def solution(strings, n):
    answer = []
    idx_n_list = []
    
    for idx in range(len(strings)):
        idx_n_list.append([strings[idx][n], idx])
    
    idx_n_list.sort(key=lambda x: (x[0], strings[x[1]]))
    
    for s, idx in idx_n_list:
        answer.append(strings[idx])
    
    return answer