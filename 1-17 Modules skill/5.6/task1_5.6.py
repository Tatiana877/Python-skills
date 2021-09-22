number_of_points = int(input("Введите количество очков: ")) 
level = 0 
if number_of_points <= 999:
  level = 1
  print('Ваш уровень: ', level)
elif number_of_points <= 2499:
  level = 2
  print('Ваш уровень: ', level)
elif number_of_points <= 4999:
  level = 3
  print('Ваш уровень: ', level)  
else:
  level = 4
  print('Ваш уровень: ', level)