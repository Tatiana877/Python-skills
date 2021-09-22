N = int(input('Введите число: '))
F = 1
for N in range(1, N+1):
  F *= N
print('Факториал числа', N, 'равен', F)