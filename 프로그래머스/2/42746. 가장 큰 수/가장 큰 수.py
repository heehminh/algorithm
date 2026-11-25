
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # numbers는 최대 1000
    
    return str(int("".join(numbers)))