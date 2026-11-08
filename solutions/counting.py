def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
        
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def arrangements(n, k):
    if k > n or n < 0 or k < 0:
        return 0
        
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result

def combinations(n, k):
    if k > n or n < 0 or k < 0:
        return 0
    if k > n // 2:
        k = n - k
        
    numerator = arrangements(n, k)
    denominator = factorial(k)
    
    return numerator // denominator
