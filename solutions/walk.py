def is_valid_walk(walk):
    if len(walk) != 10:
        return False
        
    n_count = walk.count('n')
    s_count = walk.count('s')
    e_count = walk.count('e')
    w_count = walk.count('w')
    
    if n_count == s_count and e_count == w_count:
        return True
    else:
        return False
