import datetime
# a = datetime.datetime.now()
# print(a)
# dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)

#timedelta数据类型
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))

#运算符 timedelta对象与datetime对象或者其他timedelta对象相加或相减
# dt = datetime.datetime.now()
# print(dt)
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)

# oct2lst = datetime.datetime(2015, 10, 21, 16, 29, 0)
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# print(oct2lst)
# print(oct2lst - aboutThirtyYears)
# print(oct2lst - (2 * aboutThirtyYears))

#到特定时间程序暂停
# import time
# halloween2016 =datetime.datetime(2019,11,8,0,0,0)
# while datetime.datetime.now()<halloween2016:
#     time.sleep(1)
#     print('------')

#strftime()使用类似于Python的字符串格式化
# oct2lst = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(oct2lst.strftime('%Y/%m/%d %H:%M:%S'))
# print(oct2lst.strftime('%I:%M %p'))
# print(oct2lst.strftime("%B of '%y"))

#将字符串转换成datetime对象 strptime()
# print(datetime.datetime.strptime('October 21,2015', '%B %d,%Y'))
# print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October of '15", "%B of '%y"))
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))
