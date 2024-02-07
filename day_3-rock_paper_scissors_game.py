# Rock, Paper, Scissors game

import random
import logging


def decide_winner(usr_entry, machine_entry):
    """
    :parameters: usr_entry, machine_entry:
    :returns: Output statement with information on eho one, the user or the program
    """
    usr_dict = usr_entry
    machine_dict = machine_entry
    output_statement = ""
    if usr_dict['User'] == machine_dict['Program']:
        output_statement += "It's a tie. "
        if usr_dict['User'] == 1:
            output_statement += "We both chose rock."
        elif usr_dict['User'] == 2:
            output_statement += "We both chose paper."
        else:
            output_statement += "We both chose scissors."

    elif usr_dict['User'] == 1 and machine_dict['Program'] != 1:
        if machine_dict['Program'] == 2:
            output_statement += "I win. Paper covers rock."
        else:
            output_statement += "You win. Rock crushes scissors."

    elif usr_dict['User'] == 2 and machine_dict['Program'] != 2:
        if machine_dict['Program'] == 1:
            output_statement += "You win. Paper covers rock."
        else:
            output_statement += "I win. Scissors cuts paper."
    else:
        if machine_dict['Program'] == 1:
            output_statement += "I win. Rock crushes scissors."
        else:
            output_statement += "You win. Scissors cuts paper."
    return output_statement


# Log file for the program
logging.basicConfig(filename="rock_paper_scissors.log", level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s:')

user_selection = {}
program_selection = {}

print("Rock, Paper, Scissors game.\nFor Rock enter 1. For Paper enter 2. For Scissors enter 3.\n"
      "Let\'s play")

user_entry = "invalid"

while user_entry == "invalid":
    user_selection['User'] = int(input("Choose between Rock(1), paper(2), or scissors(3):"))

    # User entry logs
    if user_selection['User'] == 1:
        logging.debug("User Input: Rock")
    elif user_selection['User'] == 2:
        logging.debug("User Input: Paper")
    elif user_selection['User'] == 3:
        logging.debug("User Input: Scissors")
    else:
        logging.debug("User Input: Invalid")

    if user_selection['User'] <= 0 or user_selection['User'] >= 4:
        print("Invalid entry. Please try again")
    else:
        user_entry = "valid"

program_output = random.randint(1, 3)
program_selection = {"Program": program_output}

# Program random choice log and console output for user
if program_selection['Program'] == 1:
    logging.debug("Program random choice: Rock")
    print("I chose rock")
elif program_selection['Program'] == 2:
    logging.debug("Program random choice: Paper")
    print("I chose paper")
else:
    logging.debug("random choice: Scissors")
    print("I chose scissors")

print(decide_winner(user_selection, program_selection))
logging.debug("Program Output: {}".format(decide_winner(user_selection, program_selection)))
