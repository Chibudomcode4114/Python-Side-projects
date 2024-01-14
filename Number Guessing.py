import  random 

def number_guessing_game():
    number_to_guess = random.randint(1,100)
    attempts = 0


    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1


        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")

        else:
            print("Too high! Try again")


number_guessing_game()


