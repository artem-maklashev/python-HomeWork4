#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from degree_dict import degree_dict
import os
def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не целое число. Повторите ввод ")
    return number

def GeneratePolinomial(number):
    poly_dict = {}
    for i in range(number+1):
        poly_dict[i] = str(randint(-100,101))
    return poly_dict

def degree(key):
    result = ''
    if key == 0 or key  == 1: 
        return ''
    elif key < 10:
        return degree_dict[key]
    else:
        degree = key
        for i in range(len(str(key))):
            result = degree_dict[degree%10] + result
            degree//=10
        return result

def ResultPolinominal(number):
    polinominal = ''
    k_polynominal = GeneratePolinomial(number)
    for i in range(number,-1,-1):
        if int(k_polynominal[i]) > 0 and i < number and i != 0:
             polinominal +='+'+ k_polynominal[i]+'x'+degree(i)
        elif  int(k_polynominal[i]) == 0:
            polinominal+=''
        elif int(k_polynominal[i]) > 0 and i == 0:
            polinominal +='+'+ k_polynominal[i]+degree(i)
        elif int(k_polynominal[i]) < 0 and i == 0:
             polinominal +=k_polynominal[i]+degree(i)
        else:
            polinominal += k_polynominal[i]+'x'+degree(i)

    polinominal+='=0'

    print(polinominal)
    return polinominal

numb = GetNumber('введите натуральную степень ')
poly = ResultPolinominal(numb)
file = open('polinominal_task2.txt','w', encoding="utf-8")
try:
    file.write(poly)
    print('polinominal_task2.txt записан')
except:
    print('Запись в файл не удалась')
file.close()



