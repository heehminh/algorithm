from itertools import permutations 

def isPrime(num):
    if num == 0 or num == 1:
        return False 
    
    for i in range(2, num):
        if num % i == 0:
            return False  
    
    return True  

def solution(numbers):
    answer = []
    
    numbers = sorted(list(numbers))
    
    for col in range(1, len(numbers)+1):
        for per in permutations(numbers, col):
            num = int("".join(per))
            
            if isPrime(num) and num not in answer:
                answer.append(num)
    
    return len(answer) 