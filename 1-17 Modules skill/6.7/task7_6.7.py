wife_check = False
number_of_hours = 0
number_of_tasks = 0
print('Начался 8-часовой рабочий день.')
while number_of_hours <= 7:
  number_of_hours += 1
  print('Час №', number_of_hours)
  task = int(input('Сколько задач решит Максим? '))
  number_of_tasks += task
  wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
  if wife == 1:
    wife_check = True
print(' ')
print('Рабочий день закончился. Всего выполнено задач: ', number_of_tasks)
if wife_check == True:
  print('Нужно зайти в магазин.')