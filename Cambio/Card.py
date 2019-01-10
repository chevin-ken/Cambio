class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.burned = False
        if ((suit == 'Diamond' or suit =='Heart') and (value == 'K')):
            self.points = -1
        elif (value == 'K'):
            self.points = 13
        elif (value == 'Q'):
            self.points = 12
        elif (value == 'J'):
            self.points = 11
        elif (value == 'A'):
            self.points = 1
        else:
            self.points = value
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in ['Diamond', 'Heart', 'Spade', 'Club']:
            for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, value))
