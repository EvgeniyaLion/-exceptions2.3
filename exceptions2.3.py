user_input = list(input('Введите оператор и два числа, разделяя их пробелами: ').split(' '))
operator = user_input[0]
assert operator in ['+', '-', '*', '/'], 'Введен неверный оператор'

val_1 = int(user_input[1])
val_2 = int(user_input[2])
result = 0
assert val_1 >= 0, 'Введено отрицательное число'
assert val_2 >= 0, 'Введено отрицательное число'
try:

    if operator == '+':
        result = val_1 + val_2
    elif operator == '-':
        result = val_1 - val_2
    elif operator == '*':
        result = val_1 * val_2
    elif operator == '/':
        result = val_1 / val_2

except ValueError:
    print('Операции со строками невозможны')
except ZeroDivisionError:
    print('Деление на 0 запрещено')
else:
    print(result)
