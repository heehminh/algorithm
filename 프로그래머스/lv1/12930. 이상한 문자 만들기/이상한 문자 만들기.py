def solution(s):
    answer = []
    words = s.split(' ')
    
    # 단어 공백을 기준으로 끊기
    for word in words:
        change_word = ''
        
        # 짝수: 대문자, 홀수: 소문자 
        for i in range(len(word)):
            if i == 0 or i % 2 == 0:
                change_word += word[i].upper()
            else:
                change_word += word[i].lower()
                
        answer.append(change_word)
    
    return ' '.join(answer)