def solution(n, words):
    end_char = words[0][-1]
    idx = 1
    
    while idx < len(words):
        word = words[idx]
        who = (idx % n) + 1
        turn = (idx // n) + 1 
        
        if word[0] == end_char and word not in words[:idx]:
            end_char = word[-1]
            idx += 1 
            
        else:
            return [who, turn]
        
    return [0, 0]