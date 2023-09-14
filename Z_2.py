'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''
number = -1
result = 'The number entered is prime'
while number < 0 or number > 100000:
    number = int(input('Input integer number fom 0 to 100000 - '))
if number == 0 or number == 1:
    result = 'The number entered is neither prime nor composite.'
else:
    for i in range(2, number):
        if number % i == 0:
            result = 'Integer number is composite'
            break
print(result)