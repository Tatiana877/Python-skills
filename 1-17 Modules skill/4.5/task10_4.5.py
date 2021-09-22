digit1 = int(input("Введите первое число: ")) 
digit2 = int(input("Введите второе число: ")) 
digit3 = int(input("Введите третье число: ")) 
if digit1 > digit2 and digit1 > digit3:
  print(digit1)
elif digit2 > digit1 and digit2 > digit3:  
  print(digit2)
else:
  print(digit3)