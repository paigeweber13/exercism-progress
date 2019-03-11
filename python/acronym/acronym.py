import re

def abbreviate(words):
    words = re.sub(r'-', ' ', words)
    words = re.sub(r'[^ a-zA-Z]', '', words)
    words = re.sub(r' +', ' ', words)
    result = ''
    firstCharacter = True
    for character in words:
        if firstCharacter:
            result += character.upper()
            firstCharacter = False
        elif character == ' ':
            firstCharacter = True
    return result
