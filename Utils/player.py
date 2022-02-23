from abc import ABC
from ast import Num
from msilib.schema import Class, Icon
from multiprocessing import Value
from optparse import Values
from random import random, shuffle
from typing_extensions import Self
from unicodedata import name

from card import Card

class Player:
    def __init__(self, name: str):
        self.name = name     
    def play(self) -> Card:
         
     card = random.choice(self.cards)
     turn_count = 13 - self.number_of_cards + 1

     self.history.append(card)
     self.cards.remove(card)
     self.number_of_cards -= 1

     
def remove_one(self):
   return self.cards.pop(0)    #to remove card from beginning of the list

player1_name = input('Enter the name of Player1: ')

player2_name = input('Enter the name of Player2: ')

player1 = Player(player1_name)
player2 = Player(player2_name)

number_of_Cards = 52     

print (f"self.name, history, self.turn_count")     

 
    
class deck:
    def __init__ (self):
        Icons = list(range(4))
        Values = list(range(13))
        for Value in Values:
           for Icon in Icons:
               self.append(Card(Value, Icon))
        return deck
    
    def shuffle(self):
      random.shuffle(self.cards)    
      return self.cards.append()  #we want the last card from deck  

    def distrubute(self, players):
        i = 0
        for a in players:
            a.cards = self.cards[i::2]
            i += 1
            a.number_of_cards = len(a.cards)
        for value in range(13):
           for player in range(4):
            print(deck)       
    def shuffle(self):
        random.shuffle(self)
        print("deck shuffled")

   

