# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))
list = []
while n > 1:
    count = 2
    while True:
        if n % count == 0:
            n = n // count
            list.append(count)
            break
        count += 1
print(list)        