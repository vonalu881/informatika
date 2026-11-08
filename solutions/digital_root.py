def digital_root(n):
    while n >= 10:
        total_sum = 0
        
        for digit_char in str(n):
            total_sum += int(digit_char)
            
        n = total_sum
        
    return n
