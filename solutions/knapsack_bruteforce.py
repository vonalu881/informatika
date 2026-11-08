def knapsack_bruteforce(items, capacity):
    def helper(index, current_capacity):
        if index == len(items) or current_capacity <= 0:
            return 0
        
        weight, val = items[index]
        cost_without_item = helper(index + 1, current_capacity)
        cost_with_item = 0

        if weight <= current_capacity:
            cost_with_item = val + helper(index + 1, current_capacity - weight)

        return max(cost_without_item, cost_with_item)
    
    return helper(0, capacity)