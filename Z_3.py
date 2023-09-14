'''
 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки.
'''

from random import randint

result = 'You didn`t guess the hidden number:('
number = randint(0, 1000)

print('Guess a number from 0 to 1000 in 10 attempts')
for i in range(1, 11):
    digit = int(input(f'Attempt № {i}. Input integer number - '))
    if number > digit:
        print('The hidden number is greater')
    elif number < digit:
        print('The hidden number is less')
    else:
        result = 'Congratulations! You guessed the hidden number.'
        break
print(result)