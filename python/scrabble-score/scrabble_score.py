import json

def load_scores(file_name = 'scores.json'):
    scores = {}
    with open(file_name) as f:
        scores = json.load(f)
    return scores

def score(word):
    word = word.lower()
    scores = load_scores()
    score = 0
    for letter in word:
        score += scores[letter]
    return score
