def square_digits(n):
    text = str(n)
    result = " "
    for char in text:
        digit = int(char)
        digit2 = digit ** 2
        result = result + str(digit2)
    return int(result)