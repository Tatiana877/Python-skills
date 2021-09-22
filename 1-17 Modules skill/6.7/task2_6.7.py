name = input('Введите Ваше имя: ')
debt = int(input('Введите сумму долга: '))
print(name,', Ваша задолженность составляет ', debt, 'руб.')
repayment_amount = int(input('Сколько рублей Вы внесёте прямо сейчас, чтобы её погасить? '))
if repayment_amount >= debt:
  print('Отлично, ', name, ', Вы погасили долг. Спасибо!')
while repayment_amount < debt:
  print('Маловато, ', name, ', давайте ещё раз.')
  repayment_amount = int(input('Сколько рублей Вы внесёте прямо сейчас, чтобы её погасить? '))
  if repayment_amount >= debt:
    print('Отлично, ', name, ', Вы погасили долг. Спасибо!')