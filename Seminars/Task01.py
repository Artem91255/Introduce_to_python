# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого

#print ('Введите первое число')
a = int(input('Введите первое число: '))
#print ('Введите второе число')
b = int(input('Введите второе число: '))

if a**2==b or b**2 ==a:
    print('одно число квадратом другого')
else:
    print('Ни одно число не является квадратом другого числа')