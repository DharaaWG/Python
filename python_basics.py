# python data types int,float,str,list,dict,tup,set,bool

#numbers
#power
print(2**3)
a=10
a=20
print(a+a)
print(type(a))

#strings
print(len('hello'))

a='heyyy'
print(a[0])
print(a[-2])

s='dhar'
l=s[1:]
print('p'+l)

x='hi this is a string'
print(x.split('i'))
print(x)

s='abcdefghijk'
print(s[2:])
print(s[:3])
print(s[3:6])
print(s[::])
print(s[::2])
print(s[2:7:2])
print(s[::-1]) #reverse a string

# a="sam" a[0]='p' not possible because strings are immutable

j='z'
print(j*10)
print(2+3)
print('2'+'3')

x='dh'
print(x.upper())
y='Hello World'
print(y.split())



print('this is a string {}'.format('INSERTED'))
print('this is a string {} {} {}'.format('a','b','c'))
print('this is a string {2} {1} {0}'.format('a','b','c'))
print('this is a string {0} {0} {0}'.format('a','b','c'))
print('this is a string {q} {b} {f}'.format(f='a',b='i',q='c'))

r=1.345888
print('the result is {a:1.3f}'.format(a=r))
print('the result is {a:10.3f}'.format(a=r))

#lists
l=[1,2,3]
m=['string',100,23.2]
m[0]='five'
print(m)

m.append('six')
print(m)
m.pop(0)
print(m)

nl=[3,5,6,1]
list=[1,1,[1,2]]
print(list[2][1])



#dict
dict={'k1':'v1','k2':'v2'}
print(dict['k1'])
dict={'k1':'v1','k2':[0,1,2],'k3':{'k1':'v1'}}
print(dict['k2'])
print(dict['k3']['k1'])
dict['k4']=300
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

#tuples
#are immutable
t=(1,2,3,'x','x','x')
a=['one',2,3]
print(t.count(3))

print(t.index('x'))

#sets
#unordered collection of unique elements
myset=set()
myset.add(1)
myset.add(2)
myset.add(1)
print(myset)
list=[1,1,1,2,2,2,1,1,3,3,4,4]
print(set(list))


#booleans
#true or false statements
k=True
print(type(k))   #T capital
print(1==1)  
b=None
print(type(b))
print(set([1,1,2,3]))

#input output with basic files  %%writefile myfile.txt

#comparisons operators
print('Bye'=='bye')
print(1== 1)
print('2'==2)
print(2==2.0)
print(3!=3)

#chaining comparison operators and or not
print(1<2>3)
print(1<2 and 2<3)
print(not 1==1)
print(1!=1)

#if elif else for
p=10
if p%2==0:
    print('even')
else:
    print('odd')

p=[1,2,3,4,5,6,7,8,9]
ol=0
for i in p:
    ol=ol+i
print(ol)    


mylist=[(1,2),(3,4)]
for a,b in mylist:
    print(a)

dict={'k1':'v1','k2':'v2'}  
for key,value in dict.items():
    print (value)  


for value in dict.values():
    print (value)  

#while
z=0
while z<5:
    print('good')
    z=z+1
else:
    print('greater than 5')

#pass
for value in x:
    pass


#continue
for letter in 'dharaa':
    if letter=='a':
        continue
    print(letter)


#range
for num in range(0,10,2):
    print(num)



word='abcde'
count=0
for letter in word:
    print(word[count])    
    count=count+1


for item in enumerate(word):
    print(item)
    

for index,letter in enumerate(word):
    print(index)
    print(letter)


ml1=[1,2,3,4,5,6]
print(min(ml1))
print(max(ml1))
from random import shuffle
from random import randint
shuffle (ml1)
print(ml1)
print (randint(0,100))

ml2=['a','b','c']
ml3=[100,200,300]   

for item in zip (ml1,ml2,ml3):
    print (item)

d={'k':45}
print(45 in d.values())

'''res=input('enter a num')
print(float(res))
res=int(input('enter a num'))
print(res)'''

mystr='hello'
mylist=[]
for letter in mystr:
    mylist.append(letter)
print(mylist)    

mylist=[letter for letter in mystr]
print(mylist)    

mylist1=[num for num in range(0,11)]
print(mylist1)  

mylist1=[num**2 for num in range(0,11)]
print(mylist1)  

mylist1=[num for num in range(0,11) if num%2==0]
print(mylist1)  

c=[0,10,20,34.5]
f=[((9/5)*temp+32)for temp in c]
print(f)

r=[x if x%2==0 else 'odd' for x in range (0,11)]
print(r)

mylist=[]
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)

mylist=[x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)



str=[1,2,3,4]
print(str.pop(2))


#functions allows us to create blocks of code that can be executed many times
def fun():
    print('hello')
fun()    

def fun(name):
    print(f'hello {name}')
fun('dharaa')    

def fun(name='default'):
    print(f'hello {name}')
fun()    
print('\n')
# print and return 
def print_fun (a,b):
    print (a+b)

def return_fun (a,b):
    return(a+b)

print(print_fun(3,5))
print(return_fun(3,5))

def even_check(num):
    res=num%2==0
    return res
print(even_check(45))  

def even_check_list(num_list):
    for num in num_list:
        if num%2==0:
            return True
        else:
             pass
print(even_check_list([1,2,3,5]))    

num_list=[1,2,3,5]
'''evennum=[]
for num in num_list:
    if num%2==0:
        evennum=evennum.append(num)
            
    else:
        pass

print(evennum)  '''

#tuple unpacking
sp=[('a',1),('b',2),('c',3)]
for t,p in sp:
    print(p)

#game
'''def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
def player_guess():
    guess=''
    while guess not in [0,1,2]:
        guess=input("enter 0,1 or 2")
    return int(guess)   

def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print('correct')  
    else :
        print('wrong guess')
        print (mylist)    

mylist=[' ','O',' ']
mixedlist=shuffle_list(mylist)
guess=player_guess()
check_guess(mixedlist,guess)'''

#*args treat them as a tuple of parameters 
# returns tuple
def func(a,b):
    return 0.05*sum((a,b))
print(func(40,60))    

def func(*args):
    return 0.05*sum(args)
print(func(40,60))    


#keyword arguments kwargs 
# returns dictionary
def func(**kwargs):
    if 'fruit' in kwargs:
        print('my choice fruit is {} '.format(kwargs['fruit']))
    else:
        print ('no fruit')    
print(func(fruit='apple'))    

#map 
def square(num):
    return num**2
my_num=[1,2,3,4,5]
for item in map(square,my_num):
    print(item)   


def splicer(mystring):
    if len(mystring)%2==0 :
        return 'even'
    else:
        return mystring[0]  
names=['andy','eve','sally']
#list(map(splicer,names))  #map executes by itself so no need to add () after splicer.map applied splicer function to every element of the list
