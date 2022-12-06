# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def ReadFile(data_name):
    data = open(data_name, 'r')
    string = data.readline()
    data.close()
    return string    

def FoundCoef(string):
    return_list = []
    list = string.split('+')
    for i in list:
        for j in range(len(i)):
            if i[j] == 'x' or i[j] == '=':
                return_list.append(i[:j])
                break
            else:
                next
    return return_list

string1 = ReadFile('file1_l4t5.txt')
string2 = ReadFile('file2_l4t5.txt')
list1 = FoundCoef(string1)
list2 = FoundCoef(string2)
if len(list1) < len(list2):
    for i in range(1, len(list1)+1):
        list2[-i] = int(list2[-i])+int(list1[-i])
        new_list = list2
else:
    for i in range(1, len(list2)+1): 
        list1[-i] = int(list1[-i])+int(list2[-i])
        new_list = list1
data = open('file3_l4t5.txt', 'w')
for i in range(len(new_list)):
    if len(new_list)-1-i == 1:
        data.writelines(f'{new_list[i]}x+')
    elif len(new_list)-1-i == 0:
        data.writelines(f'{new_list[len(new_list)-1]}=0 \n')
    else:
        data.writelines(f'{new_list[i]}x^{len(new_list)-1-i}+')
data.close()