# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = float(input('Введите число: '))
b = input('точность: ')
print(round(a, len(b.split('.')[1])))


