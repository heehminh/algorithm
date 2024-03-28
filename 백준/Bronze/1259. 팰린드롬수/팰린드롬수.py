# 펠린드롬

def is_palindrome(word):
    if (word[::-1] == word):
        return 'yes'
    else:
        return 'no'

while (True):
    word = input()
    if (word == '0'): 
        break
    
    print(is_palindrome(word))