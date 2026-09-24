from models import Player, Dealer
from game import Game
player = Player()
dealer = Dealer()
game = Game(player, dealer)
while True:
    break_outer = False
    game.round()
    print("Play Again? (Yes/No)")
    while True:
        again = input()
        if again.lower() == "yes":
            break
        elif again.lower() == "no":
            break_outer = True
            print("Thank you for playing!")
            break
        else:
            print("invalid choice")
    if break_outer:
        break