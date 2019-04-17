class Luhn(object):
    def __init__(self, card_num_string):
        self.card_num = []
        card_num_string = card_num_string.replace(' ', '')
        for char in card_num_string:
            try:
                self.card_num.append(int(char))
            except ValueError as e:
                print('only allowed input it numbers and spaces!')
                print(e)
                self.card_num = []
                return


    def is_valid(self):
        card_num_len = len(self.card_num)
        if card_num_len < 2:
            return False
        
        tmp_card_num = self.card_num.copy()
        for i in range(card_num_len - 2, -1, -2):
            tmp_card_num[i] *= 2
            if tmp_card_num[i] > 9:
                tmp_card_num[i] -= 9
        
        sum = 0
        for num in tmp_card_num:
            sum += num
        
        if sum % 10 == 0:
            return True
        else:
            return False
