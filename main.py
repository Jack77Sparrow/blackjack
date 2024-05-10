import random 

numeric_cards = list(range(2, 11))
list_of_face = ["A", "J", "Q", "K"]

coloda = numeric_cards*4 + list_of_face*4

def shuffle_cards():
    random.shuffle(coloda)
bank_roll = 100
def bank():
    return input("введите суму которую зотите поставить")

bet = bank()

def choose_cards():
    
    num1 = random.choice(coloda)    
    num2 = random.choice(coloda)
    if num1 == 'A':
        A = int(input("Введите значение для A (туза) от 1 до 11: "))
        num1 = A if 1 <= A <= 11 else 1
    elif num2 == "A":
        A = int(input("Введите значение для A (туза) от 1 до 11: "))
        num2 = A if 1 <= A <= 11 else 1

    if num1 in list_of_face and num1 != 'A':
        num1 = 10

    if num2 in list_of_face and num2 != 'A':
        num2 = 10

    print(num1, num2)
    return num1, num2



def deal_card():
    return [choose_cards() for _ in range(2)]


player1_hand = deal_card()
player2_hand = deal_card()
def player_turn(hand):
    print(sum(card[0] for card in hand))
    while sum(hand[0]) + sum(card[0] for card in hand[1:]) <= 21:
        p=0
        for player in hand:
            p+=sum(player)
        print(f"player hand {hand}   all = {p}")
        print(f"sum player {sum(card[0] for card in hand)}")
        action = input("хотите еще карту? (yes/no)")
        if action.lower() == "yes":
            hand.append(choose_cards())
        else:
            break
    
    # print(f"player hand {hand}   all = {p}")


def dealer_turn(hand):
    while sum(hand[0]) + sum(card[0] for card in hand[1:]) < 17:
        d=0
        for player in hand:
            d+=sum(player)
        print(f"рука диллера {hand}   all = {d}")
        print(f"sum dealer {sum(card[0] for card in hand)}")
        hand.append(choose_cards())
    
    # print(f"player hand {hand}   all = {d}")
    # print(f"рука диллера {hand}   all = {d}")



print(player_turn(player1_hand))

print(dealer_turn(player2_hand))


def check_black_jack(hand):
    return sum(card[0] for card in hand) == 21 and len(hand) == 2
# player1 = choose_cards()
# player2 = choose_cards()





def check_winner(player_hand, dealer_hand):
    player_sum = sum(player_hand[0]) + sum(card[0] for card in player_hand[1:])
    dealer_sum = sum(dealer_hand[0]) + sum(card[0] for card in dealer_hand[1:])
    print(f'p = {player_sum}')
    print(f"d = {dealer_sum}")
    if player_sum > 21:
        return "диллер победил", -1
    elif player_sum > 21 and dealer_sum > 21:
        return "nobody win", 0
    elif dealer_sum > 21:
        return "игрок победил", 1
    elif player_sum>dealer_sum:
        return "игрок победил", 1
    elif player_sum < dealer_sum:
        return "диллер победил", -1
    
    
    else:
        return "draw", 0
    

result, payout = check_winner(player1_hand, player2_hand)
print(result)




if payout > 0:
    bank_roll += int(bet)

elif payout < 0:
    bank_roll -= int(bet)

print(bank_roll)