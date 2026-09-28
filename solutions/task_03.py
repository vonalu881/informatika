def is_divisor(a, b):
    if (b / a) % 2 == 0:
        return True
    elif (b / a) % 2 != 0:
        return False
    else:
        return False

if __name__ == "__main__":
    a = int(input("введите а"))

if __name__ == "__main__":
    b = int(input("введите b"))

print(is_divisor(a, b))