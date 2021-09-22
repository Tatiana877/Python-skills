student = int(input('Введите число учеников: '))
five = 0
four = 0
three = 0
for i in range (1, student + 1):
  n = int(input('Введите оценку ученика: '))
  if n == 5:
    five += 1
  elif n == 4:
    four += 1
  elif n == 3:
    three += 1

if five > four and five > three:
  print('Отличников сегодня больше')
elif four > five and four > three:
  print('Хорошистов сегодня больше')
elif three > five and three > four:
  print('Троечников сегодня больше')