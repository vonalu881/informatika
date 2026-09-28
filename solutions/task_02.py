def bytes_to_kilobytes(value):
    return value / 1024

def kilobytes_to_bytes(value):
    return value * 1024

if __name__ == "__main__":
    value = float(input("введите число"))

if __name__ == "__main__":
    vbor = int(input("байты - 1, килобайты - 0"))

if vbor == 1:
    result = bytes_to_kilobytes(value)
elif vbor == 0:
    result = kilobytes_to_bytes(value)

print(result)

    


