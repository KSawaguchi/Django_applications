import random


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4

def deal():
    hand = []
    for _ in range(2):
        random.shuffle(deck)
        card = deck.pop()

        if card == 11:
            card = 'J'
        elif card == 12:
            card = 'Q'
        elif card == 13:
            card = 'K'
        elif card == 1:
            card = 'A'
        else:
            card = card

        hand.append(card)

    return hand


def hit(hand):
    random.shuffle(deck)
    card = deck.pop()

    if card == 11:
        card = 'J'
    elif card == 12:
        card = 'Q'
    elif card == 13:
        card = 'K'
    elif card == 1:
        card = 'A'
    else:
        card = card

    hand.append(card)
    return hand


def total(hand):
    score = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            score += 10
        elif card == 'A':
            if score >= 11:
                score += 1
            else:
                score += 11
        else:
            score += card
    return score


def play_again():
    again = input('もう一度プレイしますか？(Y/N):')
    if again == 'y' or again == 'Y':
        print(deck)
    else:
        print('お疲れ様でした！')


def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print('\033[91mYou Win!!\033[0m')
    elif total(player_hand) < total(dealer_hand):
        print('\033[34mYou Lose...\033[0m')
    elif total(player_hand) == total(dealer_hand):
        print('\033[34mYou Lose...\033[0m')


def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"Dealer:{dealer_hand[0]}")
    print(f"Player:{player_hand}, Ptotal:{total(player_hand)}")

    choice = 0
    while choice != quit:
        choice = input('Hit or Stand？ (H/S):').lower()
        if choice == 'h':
            hit(player_hand)
            print(f'add:{player_hand[-1]}, Ptotal:{total(player_hand)}')
            if total(player_hand) > 21:
                print('\033[34mYou Lose...\033[0m')
                choice = quit
        elif choice == 's':
            print(f'Dealer:{dealer_hand}, Dtotal:{total(dealer_hand)}')
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(f'DealerAdd:{dealer_hand[-1]}, Dtotal:{total(dealer_hand)}')
                if total(dealer_hand) > 21:
                    print('\033[91mYou Win!!\033[0m')
                    choice = quit
            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)
                choice = quit
game()