digit1 = int(input('Введите первое число: '))
digit2 = int(input('Введите второе число: '))
digit3 = int(input('Введите третье число: '))
if digit1 == digit2 == digit3:
 print('Совпало 3 числа')
elif digit1 == digit2 or digit2 == digit3 or digit1==digit3:
  print('Совпало 2 числа')   
else:
 print('Все числа различны')