def guests_by_seat(seats):
    gosti = [None] * max(seats)
    for i in range(len(seats)):
        gosti[seats[i]-1] = i + 1
    return gosti