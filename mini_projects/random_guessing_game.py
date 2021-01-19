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
        print('TODO')

    else:
        print('Input did not match prompt')


def human_game_setup():
    user_input = input('''Difficulty setting?
(E)asy: 1-100, 10 Guesses
(M)edium: 1-50, 3 Guesses
(H)ard: 1-100, 3 Guesses
(C)ustom: User defined
> ''')

    if user_input.lower() == 'easy' or 'e':
        human_game(low=1, high=100, guesses=10)

    elif user_input.lower() == 'medium' or 'm':
        human_game(low=1, high=50, guesses=3)

    elif user_input.lower() == 'hard' or 'h':
        human_game(low=1, high=100, guesses=3)

    elif user_input.lower() == 'custom' or 'c':
        low = int(input('What would you like the lower limit to be? > '))
        high = int(input('What would you like the uppper limit to be? > '))
        guesses = int(input('How many guesses would you like? >'))
        human_game(low, high, guesses)


def human_game(low, high, guesses):
    random_num = random_num_gen(low, high + 1)
    print(f'Guess a number between {low} and {high} with {guesses} guesses:')
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
    pass


def computer_game():
    pass


setup()
