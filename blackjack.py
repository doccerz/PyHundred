from card import Card
from deck import Deck


class BlackJack:

    def __init__(self):
        self.deck = None
        self.dealer = None
        self.player = None
        self.quit_check = ""
        self.round = 0
        

    def start(self):
        # Display splash
        # Ask user input for a new game
      

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
