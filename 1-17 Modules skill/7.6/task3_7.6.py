summ = 0
for salary in range (1, 13):
  salary = int(input('Введите сумму заработной платы: '))
  summ += salary
print('Среднемесячная заработная плата равна: ', summ / 12)