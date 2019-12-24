import calendar
print("Wellness fridays will be:")
year=2020
for m in range(1,13):
    cal = calendar.monthcalendar(year,m)
    week1=cal[0]
    week2=cal[1]
    week3=cal[2]
    if week1[calendar.FRIDAY] != 0:
        wf = week2[calendar.FRIDAY]
    else:
        wf = week3[calendar.FRIDAY]
    print ("%10s %2d %4s" % (calendar.month_name[m], wf, year))