def to_jaden_case(text):
    words = text.split()
    return ' '.join(word.capitalize() for word in words)
    
