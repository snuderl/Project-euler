
days = 3 * 30 + 9 * 31 + 28
years = 99

leapYears = 99 / 4

daysIn1900 = days
startingDate = 1 + days % 7
print startingDate

totalDays = days * years + leapYears

print (totalDays - 5)/7