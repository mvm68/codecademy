import random

money = 100

#Write your game of chance functions here

def check_bet(amount):
    if amount <= money and amount > 0:
        return False
    else:
        return True

def coin_flip(guess, bet):
    if check_bet(bet):
        print("CoinFlip BetError: You are betting " + str(bet) + " dollars. That is either too much or a negative number. You have " + str(money) + " dollars.")
        return 0
    if guess != "Heads" and guess != "Tails":
        print("CoinFlip GuessError: Please, guess 'Heads' or 'Tails'")
        return 0
    print("Tossing coin...")
    if random.randint(0, 1) == 0:
        result = "Heads"
    else:
        result = "Tails"
    if guess == result:
        print(result + "! You win " + str(bet) + " dollars!")
        return bet
    else:
        print(result + "... Sorry... You loose " + str(bet) + " dollars.")
        return -bet

def cho_han(guess, bet):
    if check_bet(bet):
        print("ChoHan BetError: You are betting " + str(bet) + " dollars. That is either too much or a negative number. You have " + str(money) + " dollars.")
        return 0
    if guess != "Odd" and guess != "Even":
        print("ChoHan GuessError: Please, guess 'Odd' or 'Even'")
        return 0
    print("Rolling dice for a Cho Han game...")
    if random.randint(2, 12) % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    if guess == result:
        print(result + "! You win " + str(bet) + " dollars!")
        return bet
    else:
        print(result + "... Sorry... You loose " + str(bet) + " dollars.")
        return -bet

def pick_a_card(bet):
    if check_bet(bet):
        print("CardPick BetError: You are betting " + str(bet) + " dollars. That is either too much or a negative number. You have " + str(money) + " dollars.")
        return 0
    print("Picking a card...")
    deck_n = ["Ace of Hearts", "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts", "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Spades", "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades", "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Diamonds", "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds", "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Clubs", "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs", "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"]
    deck_v = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    my_index = random.randint(0, 51)
    your_index = random.randint(0, 50)
    my_card_n = deck_n.pop(my_index)
    my_card_v = deck_v.pop(my_index)
    your_card_n = deck_n.pop(your_index)
    your_card_v = deck_v.pop(your_index)
    if my_card_v > your_card_v:
        print("You have the " + my_card_n + "...")
        print("Your opponent has the " + your_card_n + "...")
        print("Great! You win " + str(bet) + " dollars!")
        return bet
    if my_card_v < your_card_v:
        print("You have the " + my_card_n + "...")
        print("Your opponent has the " + your_card_n + "...")
        print("Sorry... You loose " + str(bet) + " dollars.")
        return -bet
    else:
        print("You have the " + my_card_n + "...")
        print("Your opponent has the " + your_card_n + "...")
        print("It's a tie! No-one wins!")
        return 0

def roulette(guess, bet):
    list_of_bets = ["Red", "Black", "Odd", "Even", "High", "Low", "Column 1", "Column 2", "Column 3", "Dozen 1", "Dozen 2", "Dozen 3", "Street 1", "Street 4", "Street 7", "Street 10", "Street 13", "Street 16", "Street 19", "Street 22", "Street 25", "Street 28", "Street 31", "Street 34", "Basket", "Snake"]
    error_message = """
    Roulette GuessError: Available bets are as follows...
    -- Any number between 0 and 36, w/out quotation marks -- Pays 35:1
    -- "Red"/ "Black" -- Pays 1:1
    -- "Odd"/ "Even" -- Pays 1:1
    -- "High"/ "Low" -- Pays 1:1
    -- "Column 1"/ "Column 2"/ "Column 3" -- Pays 2:1
    -- "Dozen 1"/ "Dozen 2"/ "Dozen 3" -- Pays 2:1
    -- "Street 1"/ "Street 4"/ "Street 7"/ .../ "Street 34" -- Pays 11:1
    -- "Basket" (a bet on numbers 0 to 3 included) -- Pays 6:1
    -- "Snake" (a bet on numbers 1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, and 34) -- Pays 2:1
    """
    if check_bet(bet):
        print("Roulette BetError: You are betting " + str(bet) + " dollars. That is either too much or a negative number. You have " + str(money) + " dollars.")
        return 0
    if guess not in range(0, 37) and guess not in list_of_bets:
        print(error_message)
        return 0
    print("Let's play roulette! Rien ne va plus!")
    print("The roulette turns... and turns... and turns...")
    result = random.randint(0, 36)
    if result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        color = "Red"
    if result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        color = "Black"
    if



    print("And the little ball lands in number " + str(result) + "!")

    if result == guess:
        print("YOU WIN A STRAIGHT BET! YOU WIN " + str(bet * 35) + " DOLLARS!")
        return bet * 35
    if guess == "Red" and result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        print(str(esult) + " is a red number! You win " + str(bet) + " dollars!")
        return bet
    if guess == "Black" and result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        print(str(esult) + " is a black number! You win " + str(bet) + " dollars!")
        return bet
    if guess == 





#Call your game of chance functions here

money += coin_flip("Heads", 20)
print("Now you have " + str(money) + " dollars.")
print()
money += cho_han("Odd", 20)
print("Now you have " + str(money) + " dollars.")
print()
money += pick_a_card(20)
print("Now you have " + str(money) + " dollars.")
print()
money += roulette(25, 20)
print("You end up with " + str(money) + " dollars.")
