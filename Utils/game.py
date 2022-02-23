from Utils.player import deck
from player import Player
from card import Card

class Board:
    """
    """
    players: list[Player] = []
    turn_count: int = 0
    active_cards: list[Card] = []
    history_cards: list[Card] = []

    def __init__(self, players: list[Player]):
        self.players = players

   
    def start_game(self):
        """
        Function that runs the game
        The deck is filled and shuffled
        A count of the cards is kept


        """
        _deck = deck()
        _deck.fill_deck()
        _deck.shuffle()
        _deck.distrubute(self.players)
        self.history = _deck
      

 