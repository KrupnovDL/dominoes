import random


def create_domino_set():
    new_domino_set = []
    for a in range(7):
        for b in range(7):
            if b >= a:
                new_domino_set.append([a, b])
    random.shuffle(new_domino_set)
    return new_domino_set


stock_pieces = create_domino_set()
computer_pieces = stock_pieces[:7]
player_pieces = stock_pieces[7:14]
stock_pieces = stock_pieces[14:]

domino_snake = None
status = None

print("Stock pieces:", stock_pieces)
print("Computer pieces:", computer_pieces)
print("Player pieces:", player_pieces)
print("Domino snake:", domino_snake)
print("Status:", status)

