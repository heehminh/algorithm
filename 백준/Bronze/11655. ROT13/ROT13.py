s = input()
ans = ''

for char in s:
    if char.isalpha():
        # 알파벳을 13만큼 밀고, 26으로 나눈 나머지를 더해서 원형 순환
        base = ord('A') if char.isupper() else ord('a')
        ans += chr((ord(char) - base + 13) % 26 + base)
        
        # if char.isupper():
        #         if chr(ord(char)+13) <= 'Z':
        #             ans += chr(ord(char)+13)
        #         else:
        #             ans += chr(ord(char)-13)
            
        # elif char.islower():
        #     if chr(ord(char)+13) <= 'z':
        #         ans += chr(ord(char)+13)
        #     else:
        #         ans += chr(ord(char)-13)
    else:
        ans += char 
        
print(ans)