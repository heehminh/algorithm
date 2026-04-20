def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            return participant[idx]
        
    return participant[-1]