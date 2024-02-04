# Guess the number game
# Main concepts: Looping, logging and random modules

import random
import logging


logging.basicConfig(filename="guess_the_number.log", level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s:')
print("Guess the number between a lower and upper limit of your choice.")

lower_limit = int(input('Please enter the lower limit:'))
upper_limit = int(input('Please enter the upper limit:'))
logging.debug("lower limit(user entry): {}".format(lower_limit))
logging.debug("upper limit(user entry): {}".format(upper_limit))


lives = 0
random_number = random.randint(lower_limit, upper_limit)
logging.debug("random number(system generated): {}".format(random_number))

while lives < 5:
    lives += 1
    guess = int(input("Enter your guess:"))
    logging.debug("guess(user entry): {}".format(guess))

    if guess == random_number:
        print("Congratulations!!! Your guess is correct.")
        break
    elif lives < 5:
        if lives == 4:
            print("Your guess is incorrect, please try again. \nYou have {} life left".format(5 - lives))
        else:
            print("Your guess is incorrect, please try again. \nYou have {} lives left". format(5-lives))
    else:
        print("Game Over. You have used up all your lives.")
