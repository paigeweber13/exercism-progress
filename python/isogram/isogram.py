def is_isogram(string):
    s = set()
    is_isogram = True
    string = string.lower()
    string = string.replace('-', '')
    string = string.replace(' ', '')
    for letter in string:
        if letter not in s:
            s.add(letter)
        else:
            is_isogram = False
    return is_isogram
