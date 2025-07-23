import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        

    def play(self):
        for round in range(0, 10):
            print(f"\nRound {round+1}")
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice not in self.choices:
                print("Invalid choice. Try again.")
                continue

            computer_choice = random.choice(self.choices)
            print(f"Computer chose: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (
                (user_choice == 'rock' and computer_choice == 'scissors') or
                (user_choice == 'scissors' and computer_choice == 'paper') or
                (user_choice == 'paper' and computer_choice == 'rock')
            ):
                print("You win this round!")
                self.user_score += 1
            else:
                print("Computer wins this round!")
                self.computer_score += 1
                

        print("\n--- Final Results ---")
        print(f"Your Score: {self.user_score}")
        print(f"Computer Score: {self.computer_score}")
        if self.user_score > self.computer_score:
            print("Congratulations! You won the game!")
        elif self.user_score < self.computer_score:
            print("Computer won the game. Better luck next time!")
        else:
            print("It's a tie overall!")

game = RockPaperScissorsGame()
game.play()
