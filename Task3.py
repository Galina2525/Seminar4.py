# Задайте два числа. Напишите программу нахождения НОК
#(наименьшее общее кратное) этих двух чисел

def nok(x,y):
    if x > y:
        smalller = y
    else:
        smalller = x
    for i in range(1,smalller + 1): # находим наибольший общий делитель
        if x % i == 0 and y % i == 0:
            max_k = i
    result = x * y / max_k        # находим НОК по формуле
    return result    
n1 = int(input('Введите первое число: '))    
n2 = int(input('Введите второе число:')) 
print(nok(n1,n2))   

