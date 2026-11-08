def count_positives_sum_negatives(numbers):
    if not numbers:
        return []
        
    positives_count = 0
    negatives_sum = 0
    
    for x in numbers:
        if x > 0:
            positives_count += 1
        elif x < 0:
            negatives_sum += x
            
    return [positives_count, negatives_sum]
