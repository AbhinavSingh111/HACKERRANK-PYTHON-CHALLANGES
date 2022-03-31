import calendar
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
m,d,y = input().split(" ")
dn = calendar.weekday(int(y),int(m),int(d))
print(days[dn])
