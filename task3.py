#  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from degree_dict import degree_dict

def koef_polynominal(polynominal):
    k = {}
    polynominal=polynominal.strip().replace('+',' +').replace('-', ' -').replace('=', ' =').split(' ')
    for i in range(len(polynominal)):
        if '**' in polynominal[i]:
            k[int(polynominal[i].split('*')[-1])] = polynominal[i].split('*')[0].replace('+', '')
        elif polynominal[i].endswith('*x'):
            k[1] = polynominal[i].split('*')[0].replace('+', '')
        elif polynominal[i].replace('-', '').replace('+', '').isdigit():
            k[0]=polynominal[i].replace('+', '')
    return k

# Преобразуем **N в нормальный вид
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

def ResultPolinominal(polynominal_1, polynominal_2):
    polinominal = ''
    result_koef = {}
    polynominal_1= koef_polynominal(polynominal_1)
    polynominal_2= koef_polynominal(polynominal_2)
    number = max(max(polynominal_1.keys()),max(polynominal_2.keys()))
    for i in range(number, -1, -1):
        result_koef[i] = int(polynominal_1.get(i))+ int(polynominal_2.get(i))
    for i in range(len(result_koef)-1, -1, -1):
        if i == len(result_koef)-1 and result_koef[i] != 0:
            polinominal+=str(result_koef[i])+'*x'+degree(i)
        elif result_koef[i] > 0 and i > 1:
            polinominal+='+'+str(result_koef[i])+'*x'+degree(i)
        elif result_koef[i] < 0 and i > 1:
            polinominal+=str(result_koef[i])+'*x'+degree(i)
        elif result_koef[i] > 0 and i == 1:
            polinominal+='+'+str(result_koef[i])+'*x'
        elif result_koef[i] < 0 and i == 1:
            polinominal+=str(result_koef[i])+'*x'
        elif result_koef[i] > 0 and i == 0:
            polinominal+='+'+str(result_koef[i])
        elif result_koef[i] < 0 and i == 0:
            polinominal+=str(result_koef[i])
    polinominal+='=0'
    polinominal=polinominal.replace('-1*x', '-x').replace('+1*x', '+x')
    return polinominal

file_1 = open('polynominal1_task3.txt','r', encoding="utf-8")
first_poly = file_1.readline()
print(first_poly)
file_2 = open('polynominal2_task3.txt','r', encoding="utf-8")
second_poly = file_2.readline()
print(second_poly)
result_poly = ResultPolinominal(first_poly, second_poly)
print(result_poly)
polinominal = open('result_polynominal_task2.txt','w', encoding="utf-8")
polinominal.write(result_poly)
polinominal.close()
