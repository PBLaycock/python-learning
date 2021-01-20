import random


def random_num_gen(low, high):
    num = random.randint(low, high)
    return num


def setup():
    print('Random number guessing game!')
    user_input = input('Human guessing or computer guessing mode? (H)uman or (C)omputer: ')

    if user_input.lower() == 'human' or user_input.lower() == 'h':
        human_game_setup()

    elif user_input.lower() == 'computer' or user_input.lower() == 'c':
        computer_game_setup()

    else:
        print('Input did not match prompt')


def human_game_setup():
    user_input = input('''Difficulty setting?
(E)asy: 1-100, 10 Guesses
(M)edium: 1-50, 3 Guesses
(H)ard: 1-100, 3 Guesses
(C)ustom: User defined
> ''')

    if user_input.lower() == 'easy' or user_input.lower() == 'e':
        human_game(lower=1, upper=100, guesses=10)

    elif user_input.lower() == 'medium' or user_input.lower() == 'm':
        human_game(lower=1, upper=50, guesses=3)

    elif user_input.lower() == 'hard' or user_input.lower() == 'h':
        human_game(lower=1, upper=100, guesses=3)

    elif user_input.lower() == 'custom' or user_input.lower() == 'c':
        low = int(input('What would you like the lower limit to be? > '))
        high = int(input('What would you like the upper limit to be? > '))
        guesses = int(input('How many guesses would you like? >'))
        human_game(low, high, guesses)


def human_game(lower, upper, guesses):
    random_num = random_num_gen(lower, upper + 1)
    print(f'Guess a number between {lower} and {upper} with {guesses} guesses:')
    tries = 0

    while tries != guesses:
        tries += 1
        user_guess = int(input('> '))

        if tries == guesses:
            print('Sorry you lost')

        elif user_guess == random_num:
            print(f'Congrats you guessed it in {tries} tries!')

        else:
            if user_guess > random_num:
                print(f'Guess is too high, you have {guesses - tries} tries left')

            if user_guess < random_num:
                print(f'Guess is too low, you have {guesses - tries} tries left')


def computer_game_setup():
    user_input = input('''Difficulty setting for computer?
    (E)asy: 1-100, 10 Guesses
    (M)edium: 1-50, 3 Guesses
    (H)ard: 1-100, 3 Guesses
    (C)ustom: User defined (Recommended)
    > ''')
    if user_input.lower() == 'easy' or user_input.lower() == 'e':
        search_type = int(input('Computer search type, 1 for random, 2 for smart random >'))
        computer_game(lower=1, upper=100, guesses=10, search_type=search_type)

    elif user_input.lower() == 'medium' or user_input.lower() == 'm':
        search_type = int(input('Computer search type, 1 for random, 2 for smart random >'))
        computer_game(lower=1, upper=50, guesses=3, search_type=search_type)

    elif user_input.lower() == 'hard' or user_input.lower() == 'h':
        search_type = int(input('Computer search type, 1 for random, 2 for smart random >'))
        computer_game(lower=1, upper=100, guesses=3, search_type=search_type)

    elif user_input.lower() == 'custom' or user_input.lower() == 'c':
        low = int(input('What would you like the lower limit to be? > '))
        high = int(input('What would you like the upper limit to be? > '))
        guesses = int(input('How many guesses would you like the computer to have? >'))
        search_type = int(input('Computer search type, 1 for random, 2 for smart random >'))
        computer_game(low, high, guesses, search_type)


def computer_game(lower, upper, guesses, search_type=2):
    random_num = random.randint(lower, upper)
    tries = 0
    current_low = lower
    current_high = upper

    while tries != guesses:
        computer_guess = computer_search(search_type, lower, upper, current_low, current_high)
        if tries == guesses:
            print("The computer lost")
            break
        elif computer_guess == random_num:
            print(f'The computer Guessed the correct number ({random_num}) in {tries} tries!')
            break
        else:
            if computer_guess > random_num:
                print(f'Guess of {computer_guess} is too high, computer has {guesses - tries} tries left')
                if current_high > computer_guess:
                    current_high = computer_guess

            if computer_guess < random_num:
                print(f'Guess of {computer_guess} is too low, computer has {guesses - tries} tries left')
                if current_low < computer_guess:
                    current_low = computer_guess
        tries += 1


def computer_search(search_type, lower, upper, current_low, current_high):
    if search_type == 1:
        computer_guess = random.randint(lower, upper)
        return computer_guess
    if search_type == 2:
        computer_guess = random.randint(current_low, current_high)
        return computer_guess


setup()
