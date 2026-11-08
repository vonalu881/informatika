def filter_numbers(items):
    result = []
    
    for x in items:
        if type(x) == int:
            result.append(x)
            
    return result
