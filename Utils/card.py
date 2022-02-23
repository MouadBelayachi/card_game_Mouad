from multiprocessing.sharedctypes import Value

from turtle import color

class Symbol:
    def __init__(self, icon, color):
        self.icon = icon
        self.color = color
        icon = [ '♥' , '♦', '♣', '♠' ]

        if icon < 2:
            self.color = "red"
        else:
            self.color = "black"


class Card(Symbol):    
    Value = ['A' , '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, icon=0, value=0):
        self.icon = icon
        self.Value = value




