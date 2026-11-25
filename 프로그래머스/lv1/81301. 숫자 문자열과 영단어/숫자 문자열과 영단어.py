def solution(s):
    strDict = { '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
                '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                '8': 'eight', '9': 'nine'}
    
    for key, value in strDict.items():
        s = s.replace(value, key) # 문자열 -> 숫자로 
    
    return int(s)