import random

# Define the deck of cards
deck = [
    "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King"
]

# Define the value of each card
card_values = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

# Define the function for drawing a card from the deck


def draw_card():
    return random.choice(deck)

# Define the function for calculating the value of a hand


def calculate_hand(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card == "Ace":
            num_aces += 1
        value += card_values[card]
    while num_aces > 0 and value <= 11:
        value += 10
        num_aces -= 1
    return value


# Start the game
print("Welcome to Blackjack!")
player_hand = [draw_card(), draw_card()]
dealer_hand = [draw_card()]
print("Your hand:", player_hand)
print("Dealer's hand:", [dealer_hand[0], "X"])

# Player's turn
while True:
    choice = input("Do you want to hit or stand? ")
    if choice.lower() == "hit":
        player_hand.append(draw_card())
        print("Your hand:", player_hand)
        if calculate_hand(player_hand) > 21:
            print("Bust! You lose.")
            break
    elif choice.lower() == "stand":
        break

# Dealer's turn
if calculate_hand(player_hand) <= 21:
    print("Dealer's hand:", dealer_hand)
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(draw_card())
        print("Dealer's hand:", dealer_hand)
    if calculate_hand(dealer_hand) > 21:
        print("Dealer busts! You win.")
    elif calculate_hand(dealer_hand) > calculate_hand(player_hand):
        print("Dealer wins! You lose.")
    elif calculate_hand(dealer_hand) < calculate_hand(player_hand):
        print("You win!")
    else:
        print("It's a tie!")
