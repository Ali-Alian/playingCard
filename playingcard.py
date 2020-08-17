"""
Created on Sun Aug 13 2020

@author: Ali Alian
"""

import random 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Card:
    def __init__(self, suit, val, CardName=""):
    
        self.suit = suit
        self.val = val
        self.CardName = CardName
        
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
 
    def show(self):
        
        if self.val == 11:
            val = "J"    # "Jack"
        elif self.val == 12:
            val = "Q"    #"Queen"
        elif self.val == 13:
            val = "K"    #"King"
        elif self.val == 1:
            val = "A"    #"Ace"
        else:
            val = self.val
        
        CardName = "{}{}.png".format(val, self.suit)
        
        
        for i in CardName:
            path1 = "data/PNG/10C.png"
            newpath = CardName
            x = path1.split("/")
            x = path1.replace(x[-1], newpath) 
            img=mpimg.imread(x)
            #print(type(newpath))
            plt.imshow(img)
        
        return CardName
    
        

        
class Deck(Card):
    
    def __init__(self):
        self.cards = []
        self.build()
    
    def show(self):
        for c in self.cards:
            c.show()
        
    def build(self):
        self.cards = []
        for e in ["S", "C", "D", "H"]:      #["Spades", "Clubs", "Diamonds", "hearts"]
            for v in range(1, 14):
                self.cards.append(Card(e, v))
                
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
            
    def drawCard(self):
        return self.cards.pop()
    
    
class Player(Card):
    
    def __init__(self, name):
        self.name = name 
        self.hand = []   # empty list to fill with player cards
    
    def P_name(self):
        print("hey my name is {}, we have a Spades, Clubs, Diamonds, hearts".format(self.name))

        
    def draw(self, deck, num=1):
        
        for i in range(num):
            self.hand.append(deck.drawCard()) #showing the random card in the player hand from Deck class 
        return self
        
    def showHand(self):
        
#        print('{}, has a : {}'.format(self.name, self.hand))
        print('{}'.format(self.hand))
        
#         for i in self.hand:
#             name = i
#             name = name.replace(" ", ".0")
#             print(name)
        
#         print(self.hand)
#         for i in self.hand:
#             print(type(i))
        
        #return self
        #c.show()
        
        #
        #return self
        #print( *self.hand)

    

# class Player(object):
#     pass

# card = Card('clubs', 8)
# card.show()

deck = Deck()
deck.shuffle()
#deck.show()

player = Player("Ali")
player.P_name()
player.draw(deck, 2)
player.showHand()
