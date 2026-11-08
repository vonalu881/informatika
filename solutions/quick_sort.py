def quick_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid_index = len(arr) // 2
    pivot = arr[mid_index]
    
    left = []
    middle = []
    right = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
            
    return quick_sort(left) + middle + quick_sort(right)
