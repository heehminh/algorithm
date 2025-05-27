s = input()
ans = ''

for char in s:
    if char.isalpha():
        if char.isupper():
                if chr(ord(char)+13) <= 'Z':
                    ans += chr(ord(char)+13)
                else:
                    ans += chr(ord(char)-13)
            
        elif char.islower():
            if chr(ord(char)+13) <= 'z':
                ans += chr(ord(char)+13)
            else:
                ans += chr(ord(char)-13)
    else:
        ans += char 
        
print(ans)