def is_balanced_number(n):
    s = str(n)
    length = len(s)
    
    def sum_of_digits(sub_str):
        total = 0
        for char in sub_str:
            total += int(char)
        return total

    if length <= 2:
        return "Balanced"
        
    side_size = (length - 1) // 2
    
    left_side = s[:side_size]
    right_side = s[length - side_size:]
    
    left_sum = sum_of_digits(left_side)
    right_sum = sum_of_digits(right_side)
    
    if left_sum == right_sum:
        return "Balanced"
    else:
        return "Not Balanced"
