summ = 0
for number in range(30, 36):
  print('Сектор № ', number)
  count = int(input('Людей в секторе: '))
  if count <= 10:
    print('Всё спокойно.')
  else:
    print('Нарушение! Слишком много людей в секторе!')
    summ +=1
print('Количество нарушений: ', summ)