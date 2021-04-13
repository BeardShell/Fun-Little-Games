import random


min_rand = 1
max_rand = 10
score = 1000
answer = 0


def play_game():
    """
    Start a new game. Explanation and start score are shown here
    """
    global answer
    answer = generate_new_number(min_rand,max_rand)
    user_guess = ask_a_guess()

def generate_new_number(min_rand,max_rand):
    return random.randint(min_rand,max_rand)

def ask_a_guess():
    user_input = input("Raad het getal: ")
    guess = int(user_input)
    evaluate_input(guess, answer)

def evaluate_input(user_input, answer):
    guess = int(user_input)
    global score

    if guess < min_rand or guess > max_rand:
        print("Blijf binnen de waardes alsjeblieft. (Groter dan {} en kleiner dan {})".format(min_rand, max_rand))
        ask_a_guess()
    elif guess == answer:
        print("Lekker bezig, {} is het goede antwoord!\nJe hebt {} punten behaald.".format(answer,score))
    else:
        print("Het door jou ingevoerde getal is niet het goede antwoord.\n")
        print(give_hint(guess,answer))
        score -= 100
        ask_a_guess()

def give_hint(user_input, answer):
    guess = int(user_input)

    if guess < answer:
        return "Het antwoord wat je zoekt is groter"
    else:
        return "Het antwoord wat je zoekt is kleiner"



if __name__ == "__main__":
    play_game()
