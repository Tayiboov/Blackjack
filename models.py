import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def value(self):
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank == "Ace":
            return 11
        else:
            return 10
class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.deck = [Card(rank,suit) for rank in ranks for suit in suits]
        random.shuffle(self.deck)
    def take(self):
        return(self.deck.pop())
class Hand:
    def __init__(self):
        self.cards = []
    def hit(self, card):
        self.cards.append(card)
    def total(self):
        total = 0
        aces = 0
        for card in self.cards:
            total += card.value()
            if card.rank == "Ace":
                aces += 1
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    def is_burst(self):
        return self.total() > 21
class Player:
    def __init__(self):
        self.hand = Hand()
    def hit_stand(self, deck):
        while True:
            print("Hit or Stand?")
            choice = input()
            if choice.lower() == "hit":
                self.hand.hit(deck.take())
                return True
            elif choice.lower() == "stand":
                return False
            else:
                print("There is no such option!")
class Dealer:
    def __init__(self):
        self.hand = Hand()
    def play(self, deck):
        while self.hand.total() < 17:
            self.hand.hit(deck.take())