import random

user_cards=[]
computer_cards=[]
is_game_over=False


def deal_card():
    """"Returns a random card form the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card



for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def compare(user_score, computer_score):
    if user_score==computer_score:
        return "draw"
    elif computer_score ==0:
        return "lose, Opponent has blackjack"
    elif user_score == 0:
        return "you with with a blackjack"
    elif user_score > 21:
        return "you went over, you lose!!"
    elif computer_score > 21:
        return "opponent went over you win!!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you lose"
    

while not is_game_over:
 
    def calculate_score(cards):
        """"Used to calculate score and blackjack."""
        #    if 11 in cards and 10 in cards and len(cards) == 2: but we can rewrite as below
        if sum(cards)==21 and len(cards)==2:
            return 0
        
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)




    user_score = calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"{user_cards} current score: {user_score}")
    print(f"Comp first card: {computer_cards[0]}")

    if user_score ==0 or computer_score==0 or user_score > 21:
            is_game_over=True
    else:
            user_should_deal=input("Type 'y' to get anohter ard, type 'n' to pass:  ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())

            else:
                is_game_over=True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    
    print(compare(user_score,computer_score))

 

