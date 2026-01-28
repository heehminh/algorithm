s = input() # 소문자

if s == s[::-1]:
    print(len(s))

else:
    for i in range(len(s)):
        p = s 
        p += s[:i+1][::-1]
        
        if p == p[::-1]:
            print(len(p))
            break