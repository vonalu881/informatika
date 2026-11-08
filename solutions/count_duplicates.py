def count_duplicates(text):
    lowered_text = text.lower()
    
    char_counts = {}
    
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    duplicates_count = 0
    for count in char_counts.values():
        if count > 1:
            duplicates_count += 1
            
    return duplicates_count
