import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def value(self):
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank == "A":
            return 11
        else:
            return 10
class Deck:
    def __init__(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["S", "H", "D", "C"]
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
            if card.rank == "A":
                aces += 1
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    def is_burst(self):
        return self.total() > 21
    def is_21(self):
        return self.total() == 21 and len(self.cards) == 2
class Player:
    def __init__(self):
        self.hand = Hand()
    def hit_stand(self, card):
        print("Hit or Stand?")
        while True:
            choice = input()
            if choice.lower() == "hit":
                self.hand.hit(card)
                break
            elif choice.lower() == "stand":
                break
class Dealer:
    def __init__(self):
        self.hand = Hand()
    def play(self, deck):
        while self.hand.total() < 17:
            self.hand.hit(deck.take())