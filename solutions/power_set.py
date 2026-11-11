def power_set(items):
    subsets = [[]]
    
    for item in items:
        new_subsets = []
        
        for current in subsets:
            new_subsets.append(current + [item])
            
        subsets.extend(new_subsets)
    
    result = []
    for s in subsets:
        result.append(tuple(s))
        
    return result