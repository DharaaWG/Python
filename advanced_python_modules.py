from collections import Counter
#counts each item in a list
#like a dictionary
mylist=[1,1,2,2,1,3,'a','a']
print(Counter(mylist))
my1='adddff'
c=Counter(my1)
my2="count words in a sentence"
print(Counter(my2.split()))
print(c.most_common(2))

from collections import defaultdict
d={'a':10}
d=defaultdict(lambda:0)
print(d['x'])
mytuple=(10,20,30)
print(mytuple[0])
from collections import namedtuple
Dog=namedtuple('Dog',['age','breed','name'])
sammy=Dog(age=5,breed='husky',name='sam')
print(type(sammy))
print(sammy.age)


import datetime
mytime=datetime.time(2,20,1,200)
#hour min sec microsec
print(mytime)
print(mytime.microsecond)


#year month day
print(datetime.date.today())
todayy=datetime.date.today()
print(todayy.year)
print(todayy.ctime())

from datetime import datetime
mydt=datetime(2021,10,3,14,20,1)
print(mydt)
print(mydt.replace(year=2023))


from datetime import date
date1=date(2021,11,3)
date2=date(2020,11,3)
print(date1-date2)
res=date1-date2
#returns difference in number of days
print(res.days)

datetime1=datetime(2021,11,3,22,0)
datetime2=datetime(2020,11,3,12,0)
print(datetime1-datetime2)
res=datetime1-datetime2
#returns difference in number of days and time
print(res.total_seconds())

import math
v=6.78
x=5.5
y=4.5
print(math.floor(v))
print(math.ceil(x))
round(x)
round(y)
#always round off to even value

print(math.pi)
print(math.e)
from math import pi

#numpy library defined for mathematical calculations
print(math.log(math.e))
print(math.log(100,10))
# 100 is number and base is 10
print(math.sin(10))
import random
print(random.randint(0,1000))
#print(random.seed(101))
mylist1=list(range(0,20))
print(mylist1)
print(random.choice(mylist1))

#with replacement
print(random.choices(population=mylist1,k=10))

#without replacement
print(random.choices(population=mylist1,k=10))
print(random.uniform(a=0,b=100)) #floating point numbers are allowed
print(random.gauss(mu=0,sigma=1)) #takes in mean and standard deviation

#pdb python debugger
'''import pdb
x=[1,2,3]
y=2
z=3
result1=y+z
#pdb.set_trace()
#result2=y+x'''

#regular expressions conatruct generalised pattern
# (555)-555-5555 regex pattern is r"(\d{3}-\d{3}-\d{4})"
text="his phone number is"
'phone' in text
import re
pattern ='phone'
m=re.search(pattern,text)
print(m)  #finds only one match
print(m.span())
print(m.start())
print(m.end()) 

text1='heyy heyy heyy how are you' #multiple matches
matches=re.findall('heyy',text1)
print(matches)

for match in re.finditer ('heyy',text1):
    print(match.group())

text2='my phone number is 234-333-4444'
phone_no=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text2)
print(phone_no.group())
phone_no1=re.search(r'(\d{3})-(\d{3})-(\d{4})',text2)
phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
res=re.search(phone_pattern,text2)
print(res.group())
print(res.group(1))

res=re.search(r'.at','the cat int the hat sat there')
print(res)
print(re.findall(r'.at','the cat int the hat sat there'))
print(re.findall(r'at','the cat int the hat sat there'))
print(re.findall(r'...at','the cat int the hat sat there'))
print(re.findall(r'^\d','1 is a number')) #start with a number
print(re.findall(r'\d$','number is 2')) #ends with a number
ph='there are 3 4 and 5'
ph1=r'[^\d]'                       #[] exclusion syntax numbers are not included
print(re.findall(ph1,ph))

#time
def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]
func_one(10)
def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str,range(n)))
func_two(10)

import time
start_time = time.time()
result = func_one(1000000)
end_time = time.time() - start_time
elapsed_time=end_time-start_time
print(elapsed_time)

# +means it occurs one or more times


























