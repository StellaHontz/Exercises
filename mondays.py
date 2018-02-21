import datetime
from datetime import date , timedelta
monday1 = 0
months = range(1,13)
today = date.today()
yearnow = today.year
x = int(yearnow)
yearsplus = today + timedelta( 365 * 10 )
years10 = yearsplus.year
y = int(years10)
for year in range(x, y):
    for month in months:
        if date(year, month, 8).weekday() == 0:
            monday1 += 1
print(monday1)