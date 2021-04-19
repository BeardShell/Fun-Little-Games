import random

score = 1000

class Game:
    def __init__(self):
        self.min_rand = 1
        self.max_rand = 100
        self.max_attempt = 10

    def new_game(self):
        """
        Start a new game. Explanation and start score are shown here
        """
        self.answer = self.generate_new_number()
        self.ask_a_guess()

    def generate_new_number(self) -> int:
        return random.randint(self.min_rand, self.max_rand)

    def ask_a_guess(self):
        question = "Raad het getal: "
        user_input = input(question)

        while not user_input.isdigit():
            user_input = input(f"De ingevoerde waarde is geen getal. Probeer het nog een keer. {question}")

        guess = int(user_input)
        self.evaluate_input(guess)

    def evaluate_input(self, user_input : int):
        guess = int(user_input)
        global score

        if guess == self.answer:
            print(f"Lekker bezig, {self.answer} is het goede antwoord!\nJe hebt {score} punten behaald.\n")
            return

        if guess < self.min_rand or guess > self.max_rand:
            print(f"Blijf binnen de waardes alsjeblieft. (Groter dan {self.min_rand} en kleiner dan {self.max_rand})")
        else:
            print("Het door jou ingevoerde getal is niet het goede antwoord.\n")
            print(self.give_hint(guess))
            score -= 100

            if (score == 0):
                print("Je score is 0. Hierdoor ben je game over!\n")
                return
        self.ask_a_guess()

    def give_hint(self, guess : int) -> str:
        if guess < self.answer:
            return "Het antwoord wat je zoekt is groter"
        return "Het antwoord wat je zoekt is kleiner"

def main():
    game = Game()
    game.new_game()

    while True:
        play_again = input("Wil je nog een keer het spel spelen? [J/N]: ")

        if play_again.lower() == "j":
            game.new_game()
        elif play_again.lower() == "n":
            break

if __name__ == "__main__":
    main()