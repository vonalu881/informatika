def duplicate_encode(text):
    text_lower = text.lower()
    
    result = ""
    
    for char in text_lower:
        if text_lower.count(char) == 1:
            result += "("
        else:
            result += ")"
            
    return result