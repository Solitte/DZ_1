'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
'''
print('Enter the sides of the triangle')
a = float(input('Input a - '))
b = float(input('Input b - '))
c = float(input('Input c - '))
if a + b > c and a + c > b and b + c > a:
    print('Triangle exists')
    if a == b == c:
        print('Equilateral triangle')
    elif a == c or a == b or b == c:
        print('Isosceles triangle')
    else:
        print('Scalene triangle')
else:
    print('Triangle doesn`t exist')

