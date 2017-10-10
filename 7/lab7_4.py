from datetime import date

def create_calendar_page(month = date.today().month, year = date.today().year):
	calendar = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
	calendar += '   ' * date(year, month, 1).weekday() + '01'
	
	for day in range(2, 32):
		try:
			calendar += '\n' if not date(year, month, day).weekday() else ' '
			calendar += '%02d' % day
		except ValueError:
			break
	
	return calendar

print(create_calendar_page(7, 2017))
print(create_calendar_page(1))
print(create_calendar_page())
print(create_calendar_page(3))
print(create_calendar_page(04, 1992))