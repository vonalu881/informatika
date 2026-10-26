def is_power_of_two(n):
    if n <= 0:
        return False
    k = 1
    while k < n:
        k = k * 2

    return k == n