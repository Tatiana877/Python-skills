number = int(input('Введите число: '))
summ = 0
while number != 0:
  summ += 1
  number //= 10
print('Количество цифр в числе:', summ)

