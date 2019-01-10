from card import *
class Player(object):
    def __init__(self):
        self.hand = []
        self.cambio = False
    def hand_value(self):
        sum = 0
        for card in self.hand:
            sum+=card.points
        return sum
    def draw_card(self, card):
        self.hand.append(card)
