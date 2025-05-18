def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False 
    return True 


number, add = map(str, input().split())
new_number = int(add+number)

if is_prime(int(number)) and is_prime(new_number):
    print('Yes')
else:
    print('No')