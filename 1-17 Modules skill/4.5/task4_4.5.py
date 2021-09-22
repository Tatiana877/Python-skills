chair1_price = int(input("Введите цену стула 1: ")) 
chair2_price = int(input("Введите цену стула 2: ")) 
chair3_price = int(input("Введите цену стула 3: "))
total_receipt_amount = chair1_price + chair2_price + chair3_price 
if total_receipt_amount > 10000: 
  print(total_receipt_amount + total_receipt_amount * 10 / 100) 
else: 
  print(total_receipt_amount)