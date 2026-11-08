def is_strong(n):
    def get_factorial(x):
        if x == 0:
            return 1
        res = 1
        for i in range(1, x + 1):
            res *= i
        return res

    num_str = str(n)
    total_sum = 0
    
    for char in num_str:
        digit = int(char)
        total_sum += get_factorial(digit)
        
    return total_sum == n
