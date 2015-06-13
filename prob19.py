def isLeap(year):
	if(year % 400 == 0): return True
	if(year % 100 == 0): return False
	if(year % 4 == 0): return True
	return False

def daysInMonth(month, year):
	arr = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if month == 2:
		if isLeap(year):
			return 29
		else:
			return 28
	return arr[month - 1]

sundaysOnFirst = 0
dayOfWeek = 2
for year in range(1901, 2001):
	for month in range(1, 13):
		for day in range(1, daysInMonth(month, year) + 1):
			if dayOfWeek == 7 and day == 1:
				sundaysOnFirst += 1
			dayOfWeek += 1
			if dayOfWeek > 7:
				dayOfWeek = 1

print sundaysOnFirst


