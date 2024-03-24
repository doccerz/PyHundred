from card import Card
from dealer import Dealer
from deck import Deck
from player import Player


class BlackJack:

    def __init__(self):
        self.deck = None
        self.dealer = None
        self.player = None
        self.quit_check = ""
        self.round = 0

    def start(self):
        # Display splash
        self.splash()

        # Ask user input for a new game
        play = True
        while (play):
            play = input("Would you like to play a game of BlackJack? (y/n): ").lower() \
                   == 'y'
            if play:
                # initialize round
                self.new_round()

                # player turn
                player_hits = True
                while (player_hits and not self.player.bust):
                    player_hits = input(
                        "Would you like to hit? (y/n): ").lower() == 'y'
                    if player_hits:
                        self.player.hit()

                # dealer turn
                print(f"Dealer's cards: {self.dealer.cards}")
                if self.player.hand <= 21 and not self.dealer.bust:
                    self.dealer.hits()

                if self.player.hand == self.dealer.hand:
                    self.player.round_message = self.dealer.round_message = "DRAW"
                else:
                    self.evaluate(self.player, self.dealer)
                    self.evaluate(self.dealer, self.player)

                # check winner
                print("=============")
                print("Round results")
                print("=============")
                print(
                    f"Dealer's hand: {self.dealer.cards} | {self.dealer.hand} | {self.dealer.round_message}"
                )
                print(
                    f"Your hand: {self.player.cards} | {self.player.hand} | {self.player.round_message}"
                )

        print("=============")
        print("Final scores")
        print("=============")
        print(f"Dealer score: {self.dealer.score}")
        print(f"{self.player.name}'s score: {self.player.score}")

    def new_round(self):
        self.round += 1
        print(f"Round {self.round}")

        # initialize deck and players
        if self.deck == None:
            self.deck = Deck()
            self.dealer = Dealer()
            self.player = Player(input("Please enter your name: ").upper())

            for o in [self.dealer, self.player]:
                o.set_deck(self.deck)
        else:
            for o in [self.deck, self.dealer, self.player]:
                o.clear()

        print(f"Dealer score: {self.dealer.score}")
        print(f"{self.player.name}'s score: {self.player.score}")

        # deal cards
        for i in range(2):
            self.player.hit()
            self.dealer.hit()

        print("Dealer's cards: ", self.dealer.facedown)
        print("Your cards: ", self.player.cards)

    def evaluate(self, player, opponent):
        if (not player.bust
                and (opponent.bust or (opponent.hand < player.hand))):
            if not opponent.bust:
                opponent.round_message = "LOSER"
            player.round_message = "WINNER"
            player.wins()

    @staticmethod
    def splash():
        art = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """
        print(art)
