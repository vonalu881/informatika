def is_tidy(n):
    num_str = str(n)
    
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            return False
            
    return True
