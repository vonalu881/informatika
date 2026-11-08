from itertools import product

def truth_table(n):
    values = [0, 1]
    
    result = list(product(values, repeat=n))
    
    return result