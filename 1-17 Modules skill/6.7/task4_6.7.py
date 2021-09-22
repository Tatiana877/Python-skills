number = int(input('Введите число дней месяца: '))
summ_even_digits = -1
while number != 0:
  number = int(input('Введите число дней месяца: '))
  if number % 2 == 0:
    summ_even_digits += 1
  if number == 0:
    print('Год завершен')
    print('Количество месяцев с четным количеством дней :', summ_even_digits)