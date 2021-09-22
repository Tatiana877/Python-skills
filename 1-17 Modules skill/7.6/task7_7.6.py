a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
summ = 0
total_number = 0
for i in range (a, b + 1):
  if i % 3 == 0:
    summ += i
    total_number += 1
    i += 1
print(summ / total_number)