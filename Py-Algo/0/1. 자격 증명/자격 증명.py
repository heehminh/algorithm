def solution(data):
    result = ''
    
    for i in data:
        i = i.replace('+', '1').replace('-', '0').replace(' ', '')
        result += chr(int(i, 2))
        # 2진수 -> 10진수
        # 10진수 -> 아스키코드
    
    return result

# 주어진 문자열을 1과 0으로 바꾸고 아스키코드로 바꾸기

# chr(65) -> A
# ord('A') -> 65 
# bin(65)[2:] -> 1000001 # 10진수 -> 2진수
# int(1000001, 2) -> 106 # 2진수 -> 10진수