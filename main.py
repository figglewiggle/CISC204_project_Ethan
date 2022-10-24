import game_obj
import random

# main
new_deck = game_obj.Deck()
# print(new_deck.list[51].suit)

class Game:
    def __init__(self, num_player=2, deck=game_obj.Deck()):
        self.deck = deck
        self.num_player = num_player
        self.player_decks = []

    def create_player_decks(self):
        i = 0
        while i < self.num_player:
            plyr_deck = game_obj.Deck()
            count = 0
            while count < 5:
                random_card_index = random.randint(0, len(self.deck.cards) - 1)
                suit = self.deck.cards[random_card_index].suit
                val = self.deck.cards[random_card_index].val
                plyr_deck.cards.append(self.deck.cards[random_card_index])
                self.deck.remove_card(suit, val)
                self.player_decks.append(plyr_deck)
                count += 1
            i += 1


g = Game()
g.deck.create_deck()
g.create_player_decks()
print(g.player_decks[0].cards[0].val)


        

