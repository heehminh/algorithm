def solution(elements):
    answer = set()
    n = len(elements)
    e = elements+elements
    
    for cnt in range(n):
        for i in range(n):
            answer.add(sum(e[i:i+cnt+1]))
    
    return len(answer)