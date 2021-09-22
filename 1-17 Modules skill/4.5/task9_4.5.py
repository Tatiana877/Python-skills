mileage = int(input("Введите пробег: ")) 
today_date = int(input("Введите сегодняшнее число: ")) 
digit_1 = mileage // 100
digit_2 = (mileage % 100) // 10
digit_3 = mileage % 10
sum_digit = digit_1 + digit_2 + digit_3
if sum_digit > today_date:
  print('Сброс.')
  mileage = 0
  print('Пробег:', mileage)
else:
  print('Сегодня не сломался')
  print('Пробег:', mileage)
