def weight_match(weight, gray):
    if gray:
        weight = 255 - weight
        
    if weight > 240:
        return "₩"
    elif weight > 200:
        return "W"
    elif weight > 160:
        return "N"
    elif weight > 140:
        return "O"
    elif weight > 110:
        return "C"
    elif weight > 90:
        return "o"
    elif weight > 70:
        return "i"
    elif weight > 50:
        return ":"
    elif weight > 20:
        return "."
    else:
        return " "
