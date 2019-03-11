class HighScores(object):
    scores = []

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)
    
    def personal_top_three(self):
        top_three = []
        tmp_list = self.scores
        for i in range(0,3):
            if len(tmp_list) > 0:
                tmpMax = max(tmp_list)
                top_three.append(tmpMax)
                tmp_list.remove(tmpMax)
        return top_three
