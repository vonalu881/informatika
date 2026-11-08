def max_gap(numbers):
    if len(numbers) < 2:
        return 0
        
    numbers.sort()
    
    max_diff = 0
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        
        if diff > max_diff:
            max_diff = diff
            
    return max_diff
