def solution(sizes):
    a_list = []
    b_list = []
    
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            a_list.append(sizes[i][0])
            b_list.append(sizes[i][1])
        else:
            a_list.append(sizes[i][1])
            b_list.append(sizes[i][0])
    
    return max(a_list) * max(b_list)