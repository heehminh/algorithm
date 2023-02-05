# 백준 4446번 ROT13 
# 함정: 입력은 여러 줄로 이루어져 있다. 각 줄은 100글자 이내의 문장이고, 
# ROT13으로 쓰여진 문장이다. 이 문장의 각 글자는 ASCII 문자 공백(32) 부터 ~(126)까지이다. 

vowels = ["a", "i", "y", "e", "o", "u"]
consonats = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]

while(True):
    try: 
        string = input()
        
        ans = ""
        for char in string:
            charisLower = True
            
            if char.isupper():
                charisLower = False
                char = char.lower()
            
            if (char in vowels):
                changeChar = vowels[(vowels.index(char)+3) %6]
                ans += changeChar if charisLower else changeChar.upper()

            elif (char in consonats):
                changeChar = consonats[(consonats.index(char)+10) %20]
                ans += changeChar if charisLower else changeChar.upper()
                
            else:
                ans += char
        print(ans)
    except:
        break