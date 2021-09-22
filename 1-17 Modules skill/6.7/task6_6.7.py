summ_positive_marks = 0
summ_negative_marks = 0
number = int(input('Введите оценку: '))
if number > 0:
  summ_positive_marks += 1
elif number < 0:
  summ_negative_marks += 1
else:
  print('Количество положительных чисел: ', summ_positive_marks)
  print('Количество отрицательных чисел :', summ_negative_marks)
while number != 0:
  number = int(input('Введите оценку: '))
  if number > 0:
    summ_positive_marks += 1
  elif number < 0:
    summ_negative_marks += 1
  else:
    print('Количество положительных чисел: ', summ_positive_marks)
    print('Количество отрицательных чисел :', summ_negative_marks)