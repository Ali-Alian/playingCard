import random 

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()

    def show(self):
        
        if self.val == 11:
            val = "Jack"
        elif self.val == 12:
            val = "Queen"
        elif self.val == 13:
            val = "King"
        elif self.val == 1:
            val = "Ace"
        else:
            val = self.val
        
        return "{} of {}".format(val, self.suit)
    
    
    
    
class Deck(object):
    
    def __init__(self):
        self.cards = []
        self.build()
    
    def show(self):
        for c in self.cards:
            c.show()
        
    def build(self):
        self.cards = []
        for e in ["Spades", "Clubs", "Diamonds", "hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(e, v))
                
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
            
    def drawCard(self):
        return self.cards.pop()
    
    
class Player(object):
    
    def __init__(self, name):
        self.name = name 
        self.hand = []   # empty list to fill with player cards
    
    def P_name(self):
        print("hey my name is {}".format(self.name))

        
    def draw(self, deck, num=1):
        
        for i in range(num):
            self.hand.append(deck.drawCard()) #showing the random card in the player hand from Deck class 
        return self
        
    def showHand(self):
        
        print('{}, has a : {}'.format(self.name, self.hand))
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
player.draw(deck, 4)
player.showHand()


