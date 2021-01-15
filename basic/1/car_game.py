is_car_running = False
user_quit = False
user_input = ''

print('Type "Help" to get started.')

while True:
    user_input = input().lower()
    if user_input == 'help':
        print('''Commands:
Start - starts the car
Stop - stops the game
Quit - quits game''')
    elif user_input == 'start':
        if not is_car_running:
            is_car_running = True
            print('Car started... Ready to go!')
        else:
            print('Car is already running...')
    elif user_input == 'stop':
        if is_car_running:
            is_car_running = False
            print('Car stopped.')
        else:
            print('Car is already stopped...')
    elif user_input == 'quit' or 'exit':
        break
    else:
        print('The car does not understand.')
