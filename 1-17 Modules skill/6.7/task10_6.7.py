start = 0
finish = 101
count = 0

while True:
  N = (start + finish) // 2
  print('Загаданное число равно, меньше или больше', N)
  answer = int(input('1 - равно, 2 - больше, 3 - меньше: '))
  count += 1

  if answer == 1:
    print('Я угадал!')
    break
  
  elif answer == 2:
    start = N
  
  elif answer == 3:
    finish = N

