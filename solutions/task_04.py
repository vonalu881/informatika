def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == "__main__":
    a = int(input("введите a"))
    b = int(input("введите b"))

print(swap(a, b))
