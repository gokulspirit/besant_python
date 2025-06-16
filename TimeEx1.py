import datetime
t=datetime.time(10,55,15,000000)
print("time:",t)

# time class Attributes #

print("Min:",datetime.time.min)
print("Max:",datetime.time.max)
print("Resolution:",datetime.time.resolution)

# Time Class Instance Attributes #
print("Hour:",t.hour)
print("Minutes:",t.minute)
print("Second:",t.second)
print("Microsecond:",t.microsecond)


# Time Class Instance Methods #
print("Replace:",t.replace(hour=13,minute=12))
print("isoformat:",t.isoformat())
print("Str:",t.__str__())


