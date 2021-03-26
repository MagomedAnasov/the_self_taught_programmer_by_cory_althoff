class Card():
    # class variables suits and values
    suits = ['diamonds',# ♦
             'hearts',  # ♥
             'spades',  # ♠
             'clubs']   # ♣
    values = [None, None, '2','3',
              '4','5','6','7',
              '8','9','10',
              'jack','queen',
              'king','ace']
    def __init__(self,v,s):
        """suit and value are integers"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit: # If values are equal, then suits are compared to avoid draw.
                return True
            else:
                return False
        return False
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

card1 = Card(10,2)
card2 = Card(11,3)
print (card1 < card2)

card1 = Card(10,2)
card2 = Card(11,3)
print(card1 > card2)