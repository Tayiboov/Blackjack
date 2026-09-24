from models import Deck, Hand
class Game:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer
    def hands(self):
        print("Your hand: ", *self.player.hand.cards, f" (total value: {self.player.hand.total()})")
        print("Dealer's hand: ", *self.dealer.hand.cards, f" (total value: {self.dealer.hand.total()})")
    def round(self):
        #resetting hands and deck
        self.player.hand = Hand()
        self.dealer.hand = Hand()
        self.deck = Deck()
        print("Starting a new round...")
        #dealing first cards
        for _ in range(2):
            self.player.hand.hit(self.deck.take())
            self.dealer.hand.hit(self.deck.take())
            print(self.player.hand.cards[-1])
        #checking natural blackjack
        if self.player.hand.total() == 21 and self.dealer.hand.total() == 21:
            self.hands()
            print("Huh? Draw.")
            return
        elif self.player.hand.total() == 21:
            self.hands()
            print("Blackjack! You Won!")
            return
        elif self.dealer.hand.total() == 21:
            self.hands()
            print("Blackjack! You Lost...")
            return
        while True:
            if self.player.hit_stand(self.deck):
                print(self.player.hand.cards[-1])
                if self.player.hand.is_burst():
                    self.hands()
                    print("Burst. You Lost...")
                    break
            else:
                self.dealer.play(self.deck)
                if self.player.hand.total() > self.dealer.hand.total() or self.dealer.hand.is_burst():
                    self.hands()
                    print("You Won!")
                elif self.player.hand.total() < self.dealer.hand.total():
                    self.hands()
                    print("You Lose...")
                else:
                    self.hands()
                    print("Huh? Draw.")
                break