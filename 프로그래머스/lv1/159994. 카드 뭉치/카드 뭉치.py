def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    while len(goal) > 0:
        if len(cards1) > 0 and goal[0] == cards1[0]:
            word = goal[0]
            cards1.remove(word)
            goal.remove(word)
        
        elif len(cards2) > 0 and goal[0] == cards2[0]:
            word = goal[0]
            cards2.remove(word)
            goal.remove(word)
        
        else:
            answer = 'No'
            break 

    return answer