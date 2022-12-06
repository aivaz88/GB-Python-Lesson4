# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
k = int(input('Задайте натуральную степень: '))
list = []
for i in range(k+1):
    list.append(random.randint(0, 100))
data = open('file_l4t4.txt', 'w')
for i in range(len(list)):
    if len(list)-1-i == 1:
        data.writelines(f'{list[i]}x+')
    elif len(list)-1-i == 0:
        data.writelines(f'{list[len(list)-1]}=0 \n')
    else:
        data.writelines(f'{list[i]}x^{len(list)-1-i}+')
data.close()