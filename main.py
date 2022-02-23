from Utils.player import Player
from Utils.game import Board


"""
Create 2 players
"""

p1 = Player("Mouad")
p2 = Player("BeCoder")

_players = [p1, p2]

"""
Create the board and start the game 
"""
game = Board(_players)
game.start_game()
