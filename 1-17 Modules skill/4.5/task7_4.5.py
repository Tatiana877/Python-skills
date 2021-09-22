required_amount = int(input("Введите сумму, которую хотите снять: ")) 
if required_amount % 100 > 0 and required_amount > 0:
 print('Такую сумму снять невозможно. Обратитесь в другой банкомат') 
elif required_amount < 0:
 print('Такую сумму снять невозможно.')   
else:
 print('Запрашиваемая сумма готовится к выдаче.') 