import time


def main(user_input):
    try:
        num = int(user_input)
        print(f'Your number was {num}')
    except ValueError:
        print('That was not a number!')


while True:
    user_input = input('What would you like to do?')

    if user_input.lower() not in ('quit', 'q', 'exit', 'close'):
        main(user_input)
        print()
    else:
        break

print('exiting - bye!')
time.sleep(3)
