#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .
number = int(input('Введите число : '))
list_n = list(range(-number,number + 1))
print(list_n)
positions = input('Введите позиции для умножения через пробел : ')
positions_array = [int(n) for n in positions.split()]
multi = 1
for i in positions_array:
     multi *= list_n[i]
print('Произведение элементов на позициях ',*positions_array,'равно:',multi)