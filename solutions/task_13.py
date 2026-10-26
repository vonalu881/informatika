def multiplication_table(n):
    table = []
    for i in range(1, 11):
        line = f"{n} x {i} = {n * i}"
        table.append(line)
    return table

if __name__ == "__main__":
    n = int(input("введите n"))

    print(multuplication_table(n))