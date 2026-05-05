from itertools import permutations 

def is_prime(str):
    flag = True 
    num = int(str)
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    if flag:
        return True  

def solution(numbers):
    answer = 0
    
    number_list = list(numbers)
    prime_set = set()
    
    for num in range(1, len(numbers)+1):
        for p in permutations(number_list, num):
            str = ""
            for string in p:
                str += string 
                
            if int(str) == 0 or int(str) == 1:
                continue
            
            if is_prime(str):
                prime_set.add(int(str))

    return len(prime_set)