##-----------------Program to Demonstrate Fixer Utilities-----------------------##
import string
import datetime as dt
#removing leading and lagging spaces from a data entry
print('# Removing leading and lagging spaces from a data entry #')
baddata = "Data Science with too many spaces are bad                                               "
print('>',baddata,'<')
cleandata= baddata.strip()
print('>',cleandata,'<')

#################Removing nonprintable characters from a data entry###
print('#2 Removing nonprintable characters from a data entry')
printable = set(string.printable)
baddata = " Data \/ Science with\x02 funny characters is \x10bad!!! "
cleandata=''.join(filter(lambda x: x in string.printable,baddata))
print('Bad Data : ',baddata)
print('Clean Data : ',cleandata) 

################Reformatting data entry to match specific formatting criteria
print('# 3 Reformatting data entry to match specific formatting criteria.')
baddate = dt.date(2019, 10, 31)
baddata=format(baddate,'%Y-%m-%d') 
gooddate = dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata=format(gooddate,'%d %B %Y') 
print('Bad Data : ',baddata)
print('Good Data : ',gooddata) 
