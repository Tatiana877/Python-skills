rating = int(input('Что получил по математике? '))
if 1 <= rating <= 3:
 print('Плохо. Марш учиться!')
elif 4 <= rating <= 5:
 print('Молодец! Можешь отдохнуть.')
else:
 print('Такой оценки в нашей системе нет. Попробуй еще раз')  