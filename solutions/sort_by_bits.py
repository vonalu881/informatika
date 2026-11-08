def sort_by_bits(numbers):
    def get_sort_key(num):
        bits_count = bin(num).count('1')
        
        return (bits_count, num)
    
    return sorted(numbers, key=get_sort_key)
