number_of_minutes = int(input('Введите количество минут: '))
number_of_hours = number_of_minutes // 60
remaining_minutes = number_of_minutes % 60
print('Количество часов составляет: ', number_of_hours)
print('Количество оставшихся минут составляет: ', remaining_minutes)