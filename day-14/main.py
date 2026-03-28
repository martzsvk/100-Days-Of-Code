import random
import art
import game_data

# higher or lower game
playing = True
while playing:
    want_play = input("Do you want to play the game of HIGHER or lower? Type 'yes' or 'no': ").lower()
    if want_play == "yes":
        print("\n" * 20)
        score = 0
        #continue playing if you had right answer
        continuation = True
        while continuation:
            # print logo from art
            print(art.logo)
            print(f"Your score is: {score}")
            # print A
            # random comparison A
            a_statement = random.choice(game_data.data)
            # follower's count
            a_follower_c = a_statement["follower_count"]
            #joining the dic together and without brackets
            a_statement = ", ".join([a_statement["name"], a_statement["description"], a_statement["country"]])
            print(f"Compare A: {a_statement}")
            print(a_follower_c)

            # print VS art
            print(art.vs)

            # print B
            # random comparison B
            b_statement = random.choice(game_data.data)
            # follower's count
            b_follower_c = b_statement["follower_count"]
            # joining the dic together and without brackets
            b_statement = ", ".join([b_statement["name"], b_statement["description"], b_statement["country"]])
            print(f"Compare B: {b_statement}")
            print(b_follower_c)


            # who has more followers?
            question = input("Who has more followers? Type 'A' or 'B': ").lower()

            # while loop to count player's score
            right_answer = True
            while right_answer:
                # check who has more followers
                # first half for A second half for B
                if a_follower_c > b_follower_c and question == "a" or b_follower_c > a_follower_c and question == "b":
                    score += 1
                    print(f"That's right. Current score: {score}")
                    # continuing
                    # first statement will be B
                    a_statement = b_statement
                    # we will create new second statement
                    b_statement = random.choice(game_data.data)
                    while True:
                            new_statement = ", ".join([b_statement["name"], b_statement["description"], b_statement["country"]])
                else:
                    print(f"I'm sorry but that's wrong. Final score: {score}")
                    right_answer = False
                    continuation = False

    else:
        playing = False


