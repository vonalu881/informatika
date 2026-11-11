def is_automorphic(n):
    square = n ** 2
    
    str_n = str(n)
    str_square = str(square)
    
    length = len(str_n)
    end_of_square = str_square[-length:]
    
    if end_of_square == str_n:
        return True
    else:
        return False
