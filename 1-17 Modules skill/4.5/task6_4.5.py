number1 = int(input("Кубик Кости: ")) 
number2 = int(input("Кубик владельца: "))
if number2 >= number1:
 print('Сумма: ', number1 - number2)  
 print('Костя платит')
else:
 print('Сумма: ', number1 + number2)  
 print('Владелец платит')
print('Игра окончена.')