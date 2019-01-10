from Card import *
from Player import *
import random
#Initializing the deck and discard piles
deck = []
for suit in ['Diamond', 'Heart', 'Spade', 'Club']:
    for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
        deck.append(Card(suit, value))
random.shuffle(deck)
discard = []
#Initializing players
player_one = new Player()
player_two = new Player()
player_three = new Player()
player_four = new Player()
players = {1:player_one, 2:player_two, 3:player_three, 4:player_four}
for player in players:
    for _ in range(0, 4):
        player.draw(deck.pop())
