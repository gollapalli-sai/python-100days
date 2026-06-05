import random

def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(u, c):
    if u == c: return "Draw 🙃"
    if c == 0: return "Lose, opponent has Blackjack 😱"
    if u == 0: return "Win with a Blackjack 😎"
    if u > 21: return "You went over. You lose 😭"
    if c > 21: return "Opponent went over. You win 😁"
    return "You win 😃" if u > c else "You lose 😤"

def play_game():
    user, comp = [deal_card(), deal_card()], [deal_card(), deal_card()]
    while (score := calculate_score(user)) < 21:
        print(f"\nYour cards: {user}, score: {score}")
        print(f"Computer's first card: {comp[0]}")
        if input("Type 'y' to get another card, 'n' to pass: ") == 'y':
            user.append(deal_card())
        else:
            break

    while calculate_score(comp) < 17:
        comp.append(deal_card())

    print(f"\nYour final hand: {user}, score: {calculate_score(user)}")
    print(f"Computer's final hand: {comp}, score: {calculate_score(comp)}")
    print(compare(calculate_score(user), calculate_score(comp)))

while input("\nPlay Blackjack? 'y' or 'n': ") == 'y':
    play_game()
