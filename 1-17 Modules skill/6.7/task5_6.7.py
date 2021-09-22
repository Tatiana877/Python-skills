total_ticket = int(input("Введите номер билета: ")) 
digit_1 = total_ticket // 100000
digit_2 = (total_ticket % 100000) // 10000
digit_3 = (total_ticket % 100000) % 10000 // 1000
digit_4 = (total_ticket % 100000) % 1000 // 100
digit_5 = (total_ticket % 100000) % 100 // 10
digit_6 = (total_ticket % 100000) % 10
sum_digit_1 = digit_1 + digit_2 + digit_3
sum_digit_2 = digit_4 + digit_5 + digit_6
if sum_digit_1 == sum_digit_2:
  print('Билет счастливый!')
else:
  print('Билет не относится к счастливым. Рекомендуем приобрести еще один.')
