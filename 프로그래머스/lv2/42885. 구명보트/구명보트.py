def solution(people, limit):
    answer = len(people)
    
    people.sort(reverse=True)
    left = 0
    right = len(people) - 1 
    
    while left < right:
        if people[left] + people[right] <= limit:
            answer -= 1
            left += 1
            right -= 1
        else:
            left += 1
                
    return answer