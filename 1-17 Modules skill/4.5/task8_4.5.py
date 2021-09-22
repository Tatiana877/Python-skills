worked_hours = int(input("Введите отработанные часы: ")) 
repayment_amount = int(input("Введите остаток по кредиту: ")) 
spending_on_food = int(input("Введите траты на еду: "))
salary = ((200 * worked_hours / 2**3) + worked_hours)
if salary > (repayment_amount + spending_on_food):
 print('Часов хватает. Можно отдохнуть')    
else:
 print('Часов не хватает. Придётся работать!') 