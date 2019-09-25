from random import randint


def generate(x=1, y=99):
    return randint(x, y)


def guess():
    while True:
        try:
            guessed = int(input("Guess the number generated:\t"))
            return guessed
        except ValueError:
            print("\nValue must be an integer")


def check():
    generated = generate()
    lives = 5
    count = 0
    while True:
        lives_left = lives - count
        if count == lives:
            print(f"Game over! Answer is {generated}")
            break
        else:
            if lives_left == 1:
                print(f"You have {lives_left} life left")
            else:
                print(f"You have {lives_left} lives left")
            guessed = guess()
            if guessed == generated:
                print(f"\nRight Guess!!! The number is {generated}")
                break
            elif guessed < generated and generated - guessed >= 10:
                print("\nGuess is too low")
            elif guessed < generated and generated - guessed <= 10:
                print("\nGuess is low")
            elif guessed > generated and guessed - generated >= 10:
                print("\nGuess is too high")
            elif guessed > generated and guessed - generated <= 10:
                print("\nGuess is high")
            count += 1


if __name__ == "__main__":
    print("\n"*4)
    print("""A random number has been generated.\
        \n\tYou need to guess the number!\
         \n\t\tHint: Number is between 0 and 100\n""")

    check()
