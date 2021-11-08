import game_settings
import random

#if __name__ == "__main__":
def game_start():
    # Initialize a game
    game = game_settings.Game(game_mode = 'easy', show_card=False)

    # 1) Load Deck
    dealer = game_settings.Person("Dealer")
    print("Player please enter your name:")
    player = game_settings.Person(input())

    # 2) Load Deck
    deck = game_settings.Deck(game)
    deck.Shuffle_deck()

    # 3) Setup game, 2 cards to each person
    game.start(dealer,player,deck)
    # Check for winner/loser
    game.get_Status(dealer,player,deck,False)
    game.print_scores(dealer,player)

    resume = True
    while resume:
        if input("Hit?  [Y/N]:") == 'Y':
            # Player has decided to take another card
            resume = True
            game.do_round(player,deck)
            game.get_Status(dealer,player,deck,False)
            game.print_scores(dealer,player)
            # Dealer decides to do another round
            if random.randint(1,100) % 2 == 0:
                print("Dealer has decided to hit")
                game.do_round(dealer,deck)
                game.get_Status(dealer,player,deck,False)
                game.print_scores(dealer,player)
            else:
                game.get_winner(dealer,player)
        else:
            if random.randint(1,100) % 2 == 0:
                print("Dealer has decided to hit")
                game.do_round(dealer,deck)
                game.get_Status(dealer,player,deck,False)
                game.print_scores(dealer,player)
            else:
                game.get_winner(dealer,player)