import datetime

year_1 = int(input("Input your first year: "))
month_1 = int(input("input your first month: "))
day_1 = int(input("Input your first day: "))
hour_1 = int(input("Input your first hour: "))
min_1 = int(input("Input your first minute: "))
sec_1 = int(input("Input your 1-st second: "))
msec_1 = int(input("Input your first microsecond: "))

year_2 = int(input("Input your second year: "))
month_2 = int(input("input your second month: "))
day_2 = int(input("Input your second day: "))
hour_2 = int(input("Input your second hour: "))
min_2 = int(input("Input your second minute: "))
sec_2 = int(input("Input your 2-nd second: "))
msec_2 = int(input("Input your 2-nd microsecond: "))

time1 = datetime.datetime(year_1, month_1, day_1, hour_1, min_1, sec_1, msec_1)
time2 = datetime.datetime(year_2, month_2, day_2, hour_2, min_2, sec_2, msec_2)

time_diff = abs(time1 - time2)

print(time_diff.total_seconds())