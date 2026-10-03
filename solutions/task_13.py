def multiplication_table(n):
    table = []
    for i in range(1, 11):
        xyi = f"{n} * {i} = {n * i}"

        table.append(xyi)
    return table

