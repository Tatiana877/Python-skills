p = float(input('Введите процентную ставку: '))
x = int(input('Сумма вклада в рублях (без копеек): '))
y = int(input('Введите дробную часть суммы вклада (кол-во копеек): '))
k = int(input('Введите количество лет нахождения вклада в банке: '))
counter = 1
deposit = (100 * x + y)
percent = (p * deposit) / 100
result = deposit + percent
result2 = 0
while counter != k and counter < k:
    result2 = int(result + (p * result) / 100)
    result = result2
    counter = counter + 1
print(int(result2 // 100), int(result2 % 100))

# чувствую, что неправильно, и задание было о другом. прошу еще подсказки, если так)
