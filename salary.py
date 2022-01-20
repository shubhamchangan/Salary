#calculate monthly salary on the basis of number of days worked & per day salary.

nm = input('enter your name:')
days = int(input('enter number of days worked:'))
sal = int(input('enter per day salary Rs.'))
print(nm, 'your working days in this month is', days, '& your per day salary is Rs.', sal)
print(nm, 'Your this month salary is Rs.', int(days*sal))