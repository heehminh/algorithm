cache = [0] * 251 
cache[1] = 1 
cache[2] = 3 


while True: 
    try:
        N = int(input())

        # dp(n) = dp(n-2)*2 + dp(n-1)

        def dp(n):
            if n == 0:
                return 1 
            
            if cache[n] > 0:
                return cache[n]
            
            cache[n] = dp(n-2)*2 + dp(n-1)
            return cache[n]

        print(dp(N))
        
    except EOFError:
        break 

