def pasture_area(wire, w):
    l = (wire - 2*w) / 3
    return w * l

def best_pasture(wire):
    w = wire / 4
    l = (wire - 2 * w) / 3
    area = w * l
    return (w,l,area)

print(best_pasture(100))