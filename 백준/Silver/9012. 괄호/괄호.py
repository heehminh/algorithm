T = int(input())
for _ in range(T):
    words = input()
    
    stk = []
    answer = 'YES'
    
    for w in list(words):
        if answer == 'NO':
            break    
        
        if w == '(':
            stk.append(w)
        else:
            if stk:
                s = stk.pop()
                
                if s != '(':
                    answer = 'NO'
            else:
                answer = 'NO'
    
    if stk:
        print('NO')
    else:
        print(answer)