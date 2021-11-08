import random
# Define a new list of 52 cards
class Card:
    def __init__(self,value,suit):
        # Suit; Clubs, Hearts, Diamonds, Spades
        self.suit = suit
        # Value/Rank; King = 10
        self.value = value
        
class Game:
    def __init__(self, game_mode='easy', win_score=21, min_score=0, card_limit=5, show_card=True):
        self.game_mode = game_mode
        self.win_score = win_score # Score required to win
        self.min_score = min_score # Any person with a score lower than this must draw another card
        self.card_limit = card_limit # Most cards a person can hold
        self.show_card = show_card # Shows dealers cards after setup
        self.status = True # True: Game continues, False: Game Over
    
    def print_scores(self,dealer,player):
        if self.show_card == True:
            print(dealer.name + " has scored " + str(dealer.score))
            print(player.name + " has scored " + str(player.score))
        else:
            print(player.name + " has scored " + str(player.score))
            
    def check_scores(self,dealer,player,deck):
        if dealer.score > self.win_score:
            self.status = False
            self.get_Status(dealer,player,deck,True)
        elif player.score > self.win_score:

            self.status = False
            self.get_Status(dealer,player,deck,True)
        elif player.score == self.win_score:
            self.status = False
            self.get_Status(dealer,player,deck,True)
        elif dealer.score == self.win_score:
            self.status = False
            self.get_Status(dealer,player,deck,True)   
        self.min_card_draw(dealer,player,deck)
        
    def min_card_draw(self,dealer,player,deck):
        if player.score < self.min_score:
            self.draw_card(player,deck)
            self.check_scores(dealer,player,deck)
        if dealer.score < self.min_score:
            self.draw_card(dealer,deck)
            self.check_scores(dealer,player,deck)
        
    def get_winner(self,dealer,player):
        minimum = min(player.score,dealer.score)
        if (player.score <= self.win_score) & (dealer.score > self.win_score):
            print("Player wins!")
            self.show_card = True
            self.print_scores(dealer,player)
            quit()
        elif (dealer.score <= self.win_score) & (player.score > self.win_score):
            print("Dealer wins!")
            self.show_card = True
            self.print_scores(dealer,player)
            quit()
        elif (player.score < self.win_score) & (dealer.score < self.win_score):
            if player.score < max(player.score,dealer.score):
                print("Dealer wins!")
                self.show_card = True
                self.print_scores(dealer,player)
                quit()
            else:
                print("Player wins!")
                self.show_card = True
                self.print_scores(dealer,player)
                quit()
        else:
            print("--- Game Draw ---")
            self.show_card = True
            self.print_scores(dealer,player)
            quit()
    
    def get_Status(self,dealer,player,deck,checked_this_round):
        if self.status == False:
            print("--- Game Over ---")
            self.get_winner(dealer,player)
        elif checked_this_round == False:
            self.check_scores(dealer,player,deck)
            
    def draw_card(self,person,deck):
        person.updateScore( deck.dealCard(person) )
        
    def start(self,dealer,player,deck):
        print("Drawing:")
        for i in range(1,3):
            print("\tdealer card "+ str(i))
            self.draw_card(dealer,deck)
            print("\tplayer card " + str(i))
            self.draw_card(player,deck)
    
    def do_round(self,person,deck):
        self.draw_card(person,deck)
        
       
class Person:
    def __init__(self,name):
        # Holds players cards
        self.cards = []
        # Holds players score
        self.score = 0
        # persons in-game name
        self.name = name
    
    def updateScore(self,Card):
        self.cards.append(Card)
        self.score += int(Card.value)
       
class Deck:
    def __init__(self,game):
        suits = ['Clubs','Spades','Diamonds','Hearts']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        deck = [Card(value,suit) for value in values for suit in suits]
        self.deck = deck
        
    def Shuffle_deck(self):
        random.shuffle(self.deck)
    
    def dealCard(self,person):
        temp = self.deck.pop(random.randint(0,len(self.deck)-1))
        if temp.value == 'A':
            try:
                user_input = input(person.name + " please enter ACE value:[11,1]")
                temp.value = int(user_input)
            except ValueError:
                print("Incorrect type, using 11 as a penalty")
                temp.value = 11
        if temp.value in ['J','Q','K']:
            temp.value = '10'
        return temp