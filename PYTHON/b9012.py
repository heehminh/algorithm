# 백준 9012 괄호 - 스택
T = int(input())

for _ in range(T):
    PS = input()
    s = []
    result = "YES"
    
    for i in PS:
        if i == "(":
            s.append("(")
        else:
            if len(s) != 0: 
                s.pop()
            else:
                # 닫는 괄호 ) 가 더 많은 경우 
                result = "NO"
                break
            
    if len(s) != 0: 
        # 여는 괄호 ( 가 더 많은 경우
        result = "NO"
        
    print(result)