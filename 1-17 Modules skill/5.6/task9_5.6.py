income = int(input('Введите Ваш доход: '))
if income < 10000:
  tax = income * 13 / 100
  print('Налог составит: ', tax, 'рублей.')
elif 10000 <= income <= 50000:
  tax = (income - 10000) * 20 / 100 + 10000 * 13 / 100
  print('Налог составит: ', tax, 'рублей.')
else:
  tax = (income - 50000) *30 /100 + 40000 * 20 / 100 + 10000 * 13 / 100
  print('Налог составит: ', tax, 'рублей.')