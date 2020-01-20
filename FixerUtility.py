import string
import datetime as dt
print('#1 Removing leading or lagging spaces from a data entry')
baddata = " Data Science with Too Many Spaces is Bad !!"
print('>',baddata,'<')
cleandata = baddata.strip()
print('>',cleandata,'<')

print('#2 Removing non printable Characters from a data entry')
printable = set(string.printable)
baddata = "Data\x00Science\x02 with Funny Characters is\x10 Bad !!"
print('Bad Data : ',baddata) 
cleandata = ".join(filter(lambda x:x in a string.printable.baddata))"
print('Clean Data : ',cleandata)

print('#3 Reformatting data entry to match specific criteria')
baddata = dt.date(2019,10,31)
baddata = format(baddata,'%Y-%m-%d')
gooddata = dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata = format(gooddata,'%Y-%m-%d')
print('Bad Data : ',baddata)
print('Good Data : ',gooddata)