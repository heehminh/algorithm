poly = input().rstrip()

# 1. AAAA가 들어올수있는지 확인
# 2. BB가 들어올수있는지 확인
# 3. 안되면 -1 출력 

poly = poly.replace("XXXX", "AAAA")
poly = poly.replace("XX", "BB")

print(poly if poly.count("X")==0 else -1)