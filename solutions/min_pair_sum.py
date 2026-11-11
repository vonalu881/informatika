def min_pair_sum(numbers):
    numbers.sort()
    total_sum = 0
    n = len(numbers)
    
    for i in range(n // 2):
        total_sum += numbers[i] * numbers[n - 1 - i]
        
    return total_sum
