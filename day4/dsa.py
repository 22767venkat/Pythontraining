#Array
from array import *
sai = array('i', [780,6,401])
print(sai[2])
print(sai[1]+sai[2])
print(sai[1]%2)
print(sai[:-1])
print(type(sai))

#list
sai=[6,'venkat',401,'thota',780,"sonata employee"]
print(sai[2])
print(sai[0]+sai[2])
print(sai[2]%2)
print(sai[:-1])
print(type(sai))

#tuple
s=(6,'venkat',401,'thota',780,"sonata employee")
print(s[2])
print(s[0]+s[2])
print(s[2]%2)
print(s[:-1])
print(type(s))

#set
a={6,'venkat',401,'thota',780,"sonata employee"}
print(a)
print(type(a))

#dictionary
i={"venkat": "12/10/1999","pavan": "25/10/2000","Sudheer": "08/08/2000"}
print(i["venkat"])