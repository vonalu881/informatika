def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

if __name__ == "__main__":
    a = int(input("введите a"))

if __name__ == "__main__":
    b = int(input("введите b"))

if __name__ == "__main__":
    c = int(input("введите c"))

print(max_of_three(a, b, c))