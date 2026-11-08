def greedy_knapsack(items, capacity): 
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    
    total_value = 0
    current_capacity = capacity
    
    for weight, val in sorted_items:
        if weight <= current_capacity:
            total_value += val
            current_capacity -= weight
            
    return total_value
