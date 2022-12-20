import datetime

date = datetime.datetime.today().date()
time = datetime.datetime.today().time()
date_time = datetime.datetime.today()
print(date)
print(time)
print(date_time)

x = datetime.datetime.now()

print(x)

filename = x.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(filename)
print(x.strftime('%F'))
print(x.strftime('%D'))