import random

__author__ = "Nicolas de Moura"
__date__ = "01/04/2022"
__version__ = 1.0

user_cards = []
computer_cards = []
user_score = []
computer_score = []
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(userCards, computerCards):
    global user_score
    global user_score
    global computer_cards
    global computer_score
    for i in range(0, 2):
        userCards.append(deal_card())
        computerCards.append(deal_card())
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    if user_score == 21:
        return 0
    if computer_score == 21:
        return 0
    if 11 in user_cards and sum(user_cards):
        user_cards.remove(11)
        user_cards.append(1)
    if 11 in computer_cards and computer_cards:
        computer_score.remove(11)
        computer_score.append(1)
    print(user_score)
    print(computer_score)
while True:
    print(logo)
    if calculate_score(user_cards, computer_cards) == 0:
        print("End")
    else:
        while True:
            if input("Do you want another card? Type 'Y' to accept or any other keyword to refuse: ").upper() == "Y":
                user_score += (deal_card())
                print(user_score)
                if user_score > 21:
                    print("End")
                    break
            else:
                break
        if user_score < 22:
            while True:
                if computer_score >= 17:
                    break
                else:
                    computer_score += deal_card()
                    print(f"The dealer took a card and now has {computer_score}")
        def compare(user, dealer):
            if user_score == computer_score:
                print("draw")
            elif user_score == 0:
                print("You have a blackjack and won")
            elif computer_score == 0:
                print("The dealer has a blackjack and won")
            elif user_score > 21:
                print("Your cards got over 21 and you loss")
            elif computer_score > 21:
                print("The dealer's cards got over 21 and you win")
            elif user_score > computer_score:
                print("You won")
            elif computer_score > user_score:
                print("Dealer won")
            print(f"-Final score-\nYou:{user_score}\nDealer:{computer_score}")
        compare(user_score, computer_score)
