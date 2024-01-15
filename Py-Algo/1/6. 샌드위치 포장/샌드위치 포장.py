def solution(data):
    result = 0
    # 1->2->3->4->1
    stk = []
    for i in data:
        if i == 1:
            if len(stk)==0:
                stk.append(i)
            elif stk[-1]==4:
                stk.append(i)
                result += 1
            elif stk[-1]==1:
                stk.append(i)

        elif i - stk[-1] ==1:
            stk.append(i)
        elif i - stk[-1] !=1:
            break
          
    return result