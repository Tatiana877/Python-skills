ru_exam_result = int(input('Введите количество баллов по русскому языку: '))
math_exam_result = int(input('Введите количество баллов по математике: '))
comp_sci_exam_result = int(input('Введите количество баллов по информатике: '))
overall_result = ru_exam_result + math_exam_result + comp_sci_exam_result
if overall_result >= 270:
  print('Поздравляю, ты поступил на бюджет!')
else:
  print('К сожалению, ты не прошёл на бюджет.')