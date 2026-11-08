def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
        
    counts1 = {}
    counts2 = {}
    
    for char in s1:
        if char in counts1:
            counts1[char] += 1
        else:
            counts1[char] = 1

    for char in s2:
        if char in counts2:
            counts2[char] += 1
        else:
            counts2[char] = 1
            
    return counts1 == counts2
