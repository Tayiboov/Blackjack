from models import Deck, Hand
class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
    def hands(self):
        print(f"Your hand: {', '.join(map(str, self.player.hand.cards))} (total value: {self.player.hand.total()})")
        print(f"Dealer's hand: {', '.join(map(str, self.dealer.hand.cards))} (total value: {self.dealer.hand.total()})")
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
            print(f"Your hand: {', '.join(map(str, self.player.hand.cards))} (total value: {self.player.hand.total()})")
            if self.player.hit_stand(self.deck):
                print(f"You got {self.player.hand.cards[-1]} (total value: {self.player.hand.total()})")
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