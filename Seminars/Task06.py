# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным

number = int(input('Введите цифру, обозначающую день недели: '))
if number>0 and number<6:
    print('Это будний день')
elif number==6 or number==7:
    print('Это выходной день')
else:
    print('Неправильный ввод')