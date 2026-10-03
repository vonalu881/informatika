def shortest_distance(kilometers, meters):
    if (kilometers * 1000) > meters:
        return meters
    elif (kilometers * 1000) < meters:
        return int(kilometers * 1000)
    else:
        return meters


print(shortest_distance(0.2, 900))



