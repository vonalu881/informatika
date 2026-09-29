values = []

def index_of_min(values):
    if len(values) == 0:
        return -1

    min_value = values[0]
    min_index = 0

    for i in range(1, len(values)):
        if values[i] < min_value:
            min_value = values[i]
            min_index = i

        return min_index
    
