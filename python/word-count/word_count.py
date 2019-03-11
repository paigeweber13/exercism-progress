import re

def word_count(phrase):
    counts = {}
    phrase = re.sub(r'[^a-zA-Z0-9\' ]', ' ', phrase)
    while len(phrase) > 0:
        match = re.match(r'\'[a-zA-Z0-9\']+\'', phrase)
        if match:
            word = match.group().lower()
            word = word[1:-1]
            if word not in counts:
                counts[word] = 0
            counts[word] += 1
            phrase = phrase[match.span()[1]:]
            continue
            pass
        match = re.match(r'[a-zA-Z0-9\']+', phrase)
        if match:
            word = match.group().lower()
            if word not in counts:
                counts[word] = 0
            counts[word] += 1
            phrase = phrase[match.span()[1]:]
            continue
        match = re.match(r' ', phrase)
        if match:
            phrase = phrase[match.span()[1]:]
            continue
    return counts
