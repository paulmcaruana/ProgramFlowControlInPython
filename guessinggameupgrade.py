import random

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess a number between 1 and {} or press 0 to quit: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")

