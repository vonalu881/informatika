def sum_interval(a, b):
    start = min(a, b)
    end = max(a, b)
    x = 0
    for i in range(start, end + 1):
        x = x + i
    return x

if __name__ == "__main__":
    a = int(input("введите a"))
    b = int(input("введите b"))

    print(sum_interval(a, b))



