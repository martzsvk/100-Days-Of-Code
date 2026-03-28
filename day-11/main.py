import art
import random

# list for cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# deal cards
def deal_cards():
    return random.choice(cards)

def print_p_cards():
    return f"Your cards are {players_cards}. [{total_player}]."

def print_pc_cards():
    return f"Computer's cards are {computers_cards}. [{total_pc}]"


# blackjack game
playing = True
# while loop so that we can play the game more times
while playing:
    # asking user if he wants to play blackjack
    want_play = input("Do you want to play a game of blackjack? Type 'yes' or 'no': ").lower()
    if want_play == "yes":
        # printing 20 lines to hide the start
        print("\n" * 20)
        # print blackjack art
        print(art.logo)

        # player's first and second cards
        first_card = deal_cards()
        second_card = deal_cards()
        # list for player's cards
        players_cards = [first_card,second_card]
        # cards together (player)
        total_player = first_card + second_card
        # printing player's cards
        print(print_p_cards())

        # computer's first and second cards
        first_pc = deal_cards()
        second_pc = deal_cards()
        # list for computer's cards
        computers_cards = [first_pc,second_pc]
        # cards together (computer)
        total_pc = first_pc + second_pc
        # printing computer's cards
        print(f"Computer's first card is {[computers_cards[0]]}.")

        # while loop so that we can take more than one card
        another_card = True
        while another_card:
            # if computer went over 21
            if total_pc > 21:
                # player
                print(print_p_cards())
                # computer
                print(print_pc_cards())
                # result
                print("Computer went over. You win.")
                break
            # if player went over
            elif total_player > 21:
                print("You went over. You lose.")
                break
            # player's blackjack
            elif total_player == 21:
                print("You have blackjack. You win.")
                break
            # computer's blackjack
            elif total_pc == 21:
                # player
                print(print_p_cards())
                # computer
                print(print_pc_cards())
                # result
                print("Computer has blackjack. You lose.")
                break
            # asking user if he wants another card/cards
            another_card = input("Type 'y' to hit and 'n' for stand: ").lower()
            # if player is under 21 he can take cards
            if total_player < 21:
                if another_card == "y":
                    # player's new card
                    new_cards = deal_cards()
                    # joining new cards to the player's card
                    players_cards.append(new_cards)
                    # updating player's total
                    total_player += new_cards
                    # printing player's cards
                    print(print_p_cards())
                    # computer's cards
                    print(f"Computer's first card is {[computers_cards[0]]}.")
                # if another_card == "n"
                else:
                    # computer must have total higher or equal to 17
                    # so we have to do while loop for that
                    while total_pc < 17:
                        if total_pc < 17:
                            # computer's new card
                            new_cards_pc = deal_cards()
                            # joining new cards to computer's cards
                            computers_cards.append(new_cards_pc)
                            # updating computer's cards
                            total_pc += new_cards_pc
                    # if player didn't go over 21 and has bigger sum than computer
                    if total_player < 21 and total_pc < total_player:
                        # player
                        print(print_p_cards())
                        # computer
                        print(print_pc_cards())
                        # result
                        print("You win.")
                        break
                    # if computer didn't go over 21 and has bigger sum than player
                    elif total_pc < 21 and total_player < total_pc:
                        # player
                        print(print_p_cards())
                        # computer
                        print(print_pc_cards())
                        # result
                        print("You lose.")
                        break
                    # player's blackjack
                    elif total_player == 21:
                        # player
                        print(print_p_cards())
                        # computer
                        print(print_pc_cards())
                        # result
                        print("You have blackjack. You win.")
                        break
                    # computer's blackjack
                    elif total_pc == 21:
                        # player
                        print(print_p_cards())
                        # computer
                        print(print_pc_cards())
                        # result
                        print("Computer has blackjack. You lose.")
                        break
                    # draw
                    elif total_pc == total_player:
                        # player
                        print(print_p_cards())
                        # computer
                        print(print_pc_cards())
                        # result
                        print("It's a draw.")
                        break
    elif want_play == "no":
        playing = False













