def raindrops(number):
    result = ""
    hasFactor = False
    if number % 3 == 0:
        result += "Pling"
        hasFactor = True
    if number % 5 == 0:
        result += "Plang"
        hasFactor = True
    if number % 7 == 0:
        result += "Plong"
        hasFactor = True
    if not hasFactor:
        result += str(number)
    return result
