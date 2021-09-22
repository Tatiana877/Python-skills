quarter1 = int(input('Введите сумму дохода за 1 квартал: '))
quarter2 = int(input('Введите сумму дохода за 1 квартал: '))
quarter3 = int(input('Введите сумму дохода за 3 квартал: '))
quarter4 = int(input('Введите сумму дохода за 4 квартал: '))
half_year1 = quarter1 + quarter2
half_year2 = quarter3 + quarter4
print(half_year1 / half_year2)