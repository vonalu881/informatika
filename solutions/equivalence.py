def truth_table(n):
    if n == 0:
        return [()]
        
    smaller_table = truth_table(n - 1)
    
    result = []
    for combo in smaller_table:
        result.append(combo + (0,))
    for combo in smaller_table:
        result.append(combo + (1,))
        
    return result

def are_equivalent(f, g, n):
    rows = truth_table(n)
    
    for row in rows:
        if f(*row) != g(*row):
            return False
            
    return True
