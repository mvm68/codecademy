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
    #I will use comments here, as this is going to be fairly complex code...
    #First, let's check for accuracy of `guess` and `bet`...
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
    # Once we have done our checks, lets begin the game...
    # Here we create our `result` and we inform the player of what is happening and what is the outcome...
    print("Let's play roulette! Rien ne va plus!")
    print("The roulette turns... and turns... and turns...")
    result = random.randint(0, 36)
    if result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        color = "Red"
    if result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        color = "Black"
    if result != 0 and result % 2 == 0:
        par_impar = "Even"
    if result % 2 == 1:
        par_impar = "Odd"
    if result != 0 and result <= 18:
        alto_bajo = "Low"
    if result >= 19:
        alto_bajo = "High"
    if result in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
        columna = "Column 1"
    if result in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
        columna = "Column 2"
    if result in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
        columna = "Column 3"
    if result > 0 and result <= 12:
        docena = "Dozen 1"
    if result > 12 and result <= 24:
        docena = "Dozen 2"
    if result > 24 and result <= 36:
        docena = "Dozen 3"
    if result != 0:
        if result % 3 == 0:
            calle = "Street " + str(result - 2)
        else:
            calle = "Street " + str(result - (result % 3) + 1)
    if result in [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]:
        sierpe = "Snake"
    if result not in [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]:
        sierpe = "not Snake"
    if result == 0:
        print("And the little marble lands in number " + str(result) + "!")
        print("0 is Basket and not Snake.")
    if result in range(1, 4):
        print("And the little marble lands in number " + str(result) + "!")
        print(str(result) + " is " + color + ", " + par_impar + ", " + alto_bajo + ", " + columna + ", " + docena + ", " + calle + ", Basket and " + sierpe)
    if result >= 4 and result <= 36:
        print("And the little marble lands in number " + str(result) + "!")
        print(str(result) + " is " + color + ", " + par_impar + ", " + alto_bajo + ", " + columna + ", " + docena + ", " + calle + ", not Basket and " + sierpe)
    # Now, we check the bet, inform the player if it is a winning bet or not, calculate & return the earnings...    
    if guess == result:
        print("YOU WIN A STRAIGHT BET! YOU WIN " + str(bet * 35) + " DOLLARS!")
        return bet * 35
    if result == 0:
        print("Sorry... You loose " + str(bet) + " dollars.")
        return -bet
    if guess == color:
        print(str(result) + " is a " + color + " number! You win " + str(bet) + " dollars!")
        return bet
    if guess == par_impar:
        print(str(result) + " is a " + par_impar + " number! You win " + str(bet) + " dollars!")
        return bet
    if guess == alto_bajo:
        print(str(result) + " is a " + alto_bajo + " number! You win " + str(bet) + " dollars!")
        return bet
    if guess == columna:
        print(str(result) + " is a " + columna + " number! You win " + str(bet * 2) + " dollars!")
        return bet * 2
    if guess == docena:
        print(str(result) + " is a " + docena + " number! You win " + str(bet * 2) + " dollars!")
        return bet * 2
    if guess == calle:
        print(str(result) + " is a " + calle + " number! You win " + str(bet * 11) + " dollars!")
        return bet * 11
    if guess == sierpe:
        print(str(result) + " is a " + sierpe + " number! You win " + str(bet * 2) + " dollars!")
        return bet * 2
    if guess == "Basket" and result in range(0, 4):
        print(str(result) + " is a Basket number! You win " + str(bet * 6) + " dollars!")
        return bet * 6
    else:
        print("Sorry... You loose " + str(bet) + " dollars.")
        return -bet

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
money += roulette("Snake", 20)
print()
print("You end up with " + str(money) + " dollars.")
