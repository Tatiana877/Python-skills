count = 0
for i in range (1, 11):
  number = int(input('Введите число: '))
  if number % 2 == 0 and number > 0:
    count += 1
print(count,' из 10 введённых Вами чисел являются одновременно чётными и положительными')