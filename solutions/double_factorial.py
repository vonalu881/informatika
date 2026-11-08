def double_factorial(n):
    if n == 0:
        return 1
        
    result = 1
    current = n
    
    while current > 0:
        result *= current
        current -= 2
        
    return result
