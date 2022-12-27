# Считать строку из набора чисел из файла. Напишите программу, которая показывает большее
# и меньшее число. В качестве символа разделителя используйте пробел. Результат
# записать в конец исходного файла(x1 x2)

#№ записываем добавляем и опять записываем

# with open('file.txt','w') as data:
#     data.write('2 5 7 10 3\n')
# with open('file.txt','r') as data: 
#     lst = data.read()

# new_lst = lst.split(' ')   
# #lst_int = [int(i)for i in new_lst] 
# lst_int = list(map(int,new_lst))
# max_ = max(lst_int)
# min_ = min(lst_int)

# with open('file.txt','a') as data: 
#     data.write(f'max = {max_}\n')
#     data.write(f'min = {min_}\n')


## Используем уже имеющийся файл

# with open('test.txt','r') as data:
#     data_list = list(map(int, data.read().split()))
#    # print(f'max = {max(data_list)}\n'
#      #     f'min = {min(data_list)}')
# with open('test.txt','a') as data:
    
#     data.writelines(f'max = {max(data_list)}\n')
#     data.write(f'min = {min(data_list)}\n')     

## Используем уже имеющийся файл

file_path = r'test2.txt' # в переменную кладем путь к файлу 
with open(file_path,'r') as data:
    data_list = list(map(int, data.read().split()))
with open(file_path,'a') as data:
    data.write(f'max = {min(data_list)}\n')    
    data.write(f'min = {max(data_list)}\n')    