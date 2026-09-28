def meters_to_centimeters(meters):
    return meters * 100

if __name__ == "__main__":
    distant = float(input("введите метры"))
    print("Distance in centimeters:", meters_to_centimeters(distant))
