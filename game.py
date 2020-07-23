import random


def start():
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    file = open('rating.txt', 'r')
    for line in file:
        if name in line:
            file.close()
            return int(line.split()[1])
    file.close()
    return 0


def rules():
    input_options = input()
    if input_options == '':
        return ['rock', 'paper', 'scissors']
    return input_options.split(',')


def win_condition(lst):
    result = {}
    i = 0
    for elem in lst:
        i += 1
        temp = lst[i:] + lst[:i]
        result[elem] = temp[:len(lst)//2]
    return result


def play_game(user_input, computer_input, wins):
    if user_input == computer_input:
        print(f'There is a draw ({user_input})')
        return 50
    elif user_input in wins[computer_input]:
        print(f'Well done. Computer chose {computer_input} and failed')
        return 100
    else:
        print(f'Sorry, but computer chose {computer_input}')
        return 0


user_rating = start()
options = rules()
win_rules = win_condition(options)
print("Okay, let's start")
while True:
    user_move = input()

    if user_move == '!exit':
        print('Bye!')
        break
    elif user_move == '!rating':
        print('Your rating:', user_rating)
        continue
    elif user_move in options:
        computer_move = random.choice(options)
        user_rating += play_game(user_move, computer_move, win_rules)
    else:
        print('Invalid input!')
