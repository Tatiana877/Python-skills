square = int(input('Введите площадь квартиры: '))
cost = int(input('Введите стоимость квартиры: '))
if square >= 100 and cost <= 10000000:
 print('Квартира подходит.')
elif 80 <= square < 100 and cost <= 7000000:
  print('Квартира подходит.')   
else:
 print('Квартира не подходит.')