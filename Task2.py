# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами
# 1) с помощью математических формул нахождения корней квадратного уравнения
#2) с помощью дополнительных библиотек python
import random
def squre_def(a, b, c) -> tuple|str:
    print(f'коэффициент a = {a}\n'
          f'коэффициент b = {b}\n'
          f'коэффициент c = {c}')
    discr = b ** 2 - 4 * a * c
    print(f'Дискриминант = {discr}') 
    if discr > 0:
        x1 = (-b + discr ** 0.5)/(a * a)
        x2 = (-b - discr ** 0.5)/(a * a)
        print(f'корень x1 = {x1}')
        print(f'корень x2 = {x2}')
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        print(f'Корень x = {x}')
        return x,
    return'Корней нет'

print(squre_def(a = random.randint(1, 15),
                b = random.randint(1, 15),
                c = random.randint(1,15)))



   