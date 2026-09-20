secret = 42
attempts = 0

while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess == secret:
        print(f"correct! You guessed the secret number in {attempts} attempts.")
        break
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")