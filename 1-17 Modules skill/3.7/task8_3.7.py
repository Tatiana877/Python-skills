digit = int(input('Введите четырёхзначное число: '))
remains1 = digit // 1000
remains2 = (digit // 100) % 10
remains3 = (digit % 100) // 10
remains4 = digit % 10
print(remains1, remains2, remains3, remains4)