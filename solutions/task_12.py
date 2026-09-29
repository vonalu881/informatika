def shortest_distance(kilometers, meters):
    if (kilometers * 1000) > meters:
        return meters
    elif (kilometers * 1000) < meters:
        return kilometers * 1000
    else:
        return meters

if __name__ == "__main__":
    kilometers = float(input("введите километры"))

if __name__ == "__main__":
    meters = float(input("введите метры"))

    print(shortest_distance(kilometers, meters))



