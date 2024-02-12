# Hangman Game: African countries edition

import pandas as pd
import random
import logging


def country_name_as_list(country_name):
    country_name_ = []
    for chars in country_name:
        country_name_.append(chars)
    return country_name_


def specific_letters_in_country_name(country_name):
    letters_in_country_name = []
    for chars in country_name:
        if chars.isalpha():
            letters_in_country_name.append(chars)
    return letters_in_country_name


def display_user_progress(country_name, user_progress, guessed_letter):
    updated_user_progress = []

    for index_ in range(len(country_name)):
        if country_name[index_].isalpha() and country_name[index_] == guessed_letter \
                and user_progress[index_] != "*":
            user_progress[index_] = "*"
            break

    for index_ in range(len(country_name)):
        if country_name[index_].isalpha() and user_progress[index_] == "_ ":
            updated_user_progress.append("_ ")
        elif country_name[index_].isalpha() and user_progress[index_] == "*":
            updated_user_progress.append(country_name[index_])
        else:
            updated_user_progress.append(country_name[index_])
    return [user_progress, updated_user_progress]


def validate_guess(character):
    if character.isalpha():
        validated_guess = character.lower()
        return validated_guess
    else:
        return "invalid"


def guessed_letter_in_name(character, letters_left):
    if character not in letters_left:
        return ["incorrect", letters_left, character]
    else:
        letters_left.remove(character)
        return ["correct", letters_left]


def word_complete(letters_left):
    if len(letters_left) > 0:
        return "incomplete"
    elif len(letters_left) == 0:
        return "complete"


logging.basicConfig(filename="hangman_game.log", level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s:')

countries_dataframe = pd.read_excel('countries_in_africa_data.xlsx', usecols='B')
countries_list = countries_dataframe['country'].tolist()
random_country_selected = random.choice(countries_list)
logging.debug("Random country selected: {}".format(random_country_selected))

lowercase_name = random_country_selected.casefold()
country_name_as_list = country_name_as_list(lowercase_name)
letters_in_name = specific_letters_in_country_name(lowercase_name)

incorrect_letters_guessed = []
initial_progress_display = []
display_progress = []
current_guess = []
attempts = 6

for char in lowercase_name:
    if char.isalpha():
        initial_progress_display.append("_ ")
    else:
        initial_progress_display.append(char)

print("\nHangman Game: African country edition.\n\nGuess the African nation by filling in letters in the name.")
print("Country: {}. [{} letters]".format(''.join(initial_progress_display), len(letters_in_name)))
display_progress = (display_user_progress(country_name_as_list, initial_progress_display, ""))

while attempts > 0:
    user_guess = input("Guess a letter in the name:")
    logging.debug("User guess: {}".format(user_guess))
    if validate_guess(user_guess) == "invalid":
        print("Invalid guess. Only letters of the alphabet are allowed.\nPlease try again!")
    else:
        guess = validate_guess(user_guess)
        guess_correct = guessed_letter_in_name(guess, letters_in_name)
        if guess_correct[0] == "correct":
            if word_complete(guess_correct[1]) == "complete":
                display_progress = display_user_progress(country_name_as_list, display_progress[0], guess)
                print("Current progress: {}".format(''.join(display_progress[1])))
                print("You've guessed all the letters. You win.")
                print("Incorrect letters guessed: {}".format(incorrect_letters_guessed))
                break
            elif word_complete(guess_correct[1]) == "incomplete":
                print("Correct. Guess the remaining letters")
                display_progress = display_user_progress(country_name_as_list, display_progress[0], guess)
                print("Current progress: {}".format(''.join(display_progress[1])))
                print("Incorrect letters guessed: {}".format(incorrect_letters_guessed))
        elif guess_correct[0] == "incorrect":
            attempts -= 1
            incorrect_letters_guessed.append(guess)
            print("Wrong guess.")
            if attempts == 0:
                print("Incorrect letters guessed: {}".format(incorrect_letters_guessed))
                display_progress = display_user_progress(country_name_as_list, display_progress[0], guess)
                print("Current progress: {}".format(''.join(display_progress[1])))
                print("You have run out of guesses. Game Over!\nThe country was {}".format(random_country_selected))
                break
            else:
                print("Please try again")
                print("Incorrect letters guessed: {}".format(incorrect_letters_guessed))
                display_progress = display_user_progress(country_name_as_list, display_progress[0], guess)
                print("Current progress: {}".format(''.join(display_progress[1])))
