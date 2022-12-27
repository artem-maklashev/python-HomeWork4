# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = float(input(message))
            if number <= 10**(-1) and number >= 10**(-10):
                isCorrect = True
            else:
                print('Точность не соответствует заданному диапазону. Повторите ввод ')
        except ValueError:
            print("Введено не число. Повторите ввод ")
    return number

def FloatPoint(number):
    precision = 0
    while number <1:
        number*=10
        precision+=1
    print('10.'+str(precision)+'f')
    result = round(pi, precision)
    return result

numb = GetNumber('Введите точность в диапазоне 10^{-10} ≤ d ≤10^{-1} в формате 0.001... ')
x = (FloatPoint(numb))
print(f'при d = {numb} π = {x}')
