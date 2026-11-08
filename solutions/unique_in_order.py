def unique_in_order(sequence):
    result = []
    
    for item in sequence:
        if len(result) == 0 or item != result[-1]:
            result.append(item)
            
    return result
