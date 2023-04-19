while True:
    str = input()
    
    if str == ".":
        break
    
    result = "yes"
    
    stk = []
    
    for i in list(str):

        if (i != "."):
            if (i == "("):
                stk.append("(")
            elif (i == ")"):
                if (stk and stk[-1]=="("):
                    stk.pop()
                else: 
                    result = "no"
            elif (i == "["):
                stk.append("[")
            elif (i == "]"):
                if (stk and stk[-1]=="["):
                    stk.pop() 
                else: 
                    result = "no"
            
    if (stk):
        result = "no"
    
    print(result)
            