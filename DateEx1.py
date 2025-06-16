import datetime
import time
d=datetime.date(2021,6,24)
print("Current Date:",d)
print(d.strftime("%c"))

print("Today:",datetime.date.today())
print("TimeStamp:",datetime.date.fromtimestamp(time.time()))

# Date Class Attributes #
print("Min:",datetime.date.min)
print("Max:",datetime.date.max)
print("Resolution:",datetime.date.resolution)

# Date Class Instance Attributes #
print("Year:",d.year)
print("Month:",d.month )
print("Day:",d.day )


# Date Class Instance Methods #
#d=d.replace(month=5)
print("Date After Replace:",d.replace(year=2022,month=6,day=13))
print("Time Tuple:",d.timetuple())
print("Weekday:",d.weekday())
print("IsoWeekday:",d.isoweekday())
print("isocalendar:",d.isocalendar())
print("isoformat:",d.isoformat())
print("Str:",d.__str__())
print("ctime:",d.ctime ())



