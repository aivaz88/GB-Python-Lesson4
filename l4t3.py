# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

list = [1, 2, 3, 4, 2, 6, 1, 7, 7, 4, 9]
newList = []
for i in list:
    if i in newList:
        next
    else:
        newList.append(i)
print(list)
print(newList)