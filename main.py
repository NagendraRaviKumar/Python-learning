from typing import Set, Any

from mathematics.maths import *
import random


x = 4       # x is of type int
x = "Sally"  # x is now of type str
print(x)
fruits = ["apple", "banana", "cherry"]
x,y, z = fruits
print(x)
print(y)
print(z)
#addition of x,y
x = 8
y = 1
print(x+y)
x = 3.0
z = 3.787876940
print (type(x))
print (type(z))
x= "nice"

def myfunc():
    print("looking " +x)
myfunc()

z= "fantastic"
def myfunc(z):
    print("looking" +z)
myfunc(z)

print(random.randrange(1,6))

txt= "students are studying well"
print("well"in txt)
txt= "students are studying well"
if "well" in txt:
    print("yes,statement is correct")
txt= "himalays is such a beautiful place"
print("expensive" not in txt)
txt= "himalays is such a beautiful place"
if "well" not in txt:
    print("yes,statement is true")
a= "hello world"
print(a[2:4])
print(a[-3:-1])
print(a.upper())
print(a.lower())
b= "Hello world  "
print(b.strip())
x= "my name is kalyan"
print(x.split())
z= "my name is kalyan"
print(z.replace ("kalyan", "pavan"))
x= "Thank"
y= "you"
print(x+y)
print(x+" "+y)
age= 45
txt= "My name is ramu  age is {}"
print(txt.format(age))
quantity = 3
item = 567
price = 49.95
myorder="I want {0} pieces of item {1} for {2}dollrs"
print(myorder.format(quantity,item,price))
x= 10
y= 5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
x=5
x+=5
print(x)
x=6
print(x>3 and x<8)
print(x<3 or x<8)
print(not(x>3 and x<8))
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x==y)
print(x is not z)
print(x is not y)
print(x!=y)
B = ["apple","pineapple","sapota"]
print("pineapple" in B)
print("kiwi" not in B)
mylist = {"boy","girl","toy"}
print(type(mylist))
thelist=["boy","king","girl"]
thelist[2]= ("smart")
print(thelist)
thelist=["boy","king","girl","queen"]
thelist.insert(2,"was")
print(thelist)
thislist= ["apple", "banana", "cherry"]
for el in thislist:
  print(el)
even =[1,2,3,4,5,6,7,8]
for el in even:
    if el%2 ==0:
        print(el)
thislist= ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
thislist = ["king", "queen"]
[ print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x :
        newlist.append(x)
print(newlist)
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist= [ x for x in fruits if "a" in x]
print(newlist)
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x if x !="cherry" else "orange" for x in fruits ]
print(newlist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
thislist = ["banana","kiwi","mango","Pineapple","sapota"]
thislist.sort()
print(thislist)
thislist.sort(key=str.lower)
print(thislist)
thislist = ["kiwi","mango","pineapple","sapota"]
thislist.sort()
print(thislist)
thislist = ["kiwi","mango","pineapple",]
mylist = thislist.copy()
print(mylist)
mytuple=("apple")
print(type(mytuple))
mytuple=("apple",)
print(type(mytuple))
thistuple = ["kiwi","mango","pineapple",]
print(thistuple[2])
print(thistuple[-3])
mytuple = ("mango","kiwi","straberry","grapes")
y =list(mytuple)
y.append("orange")
mytuple=tuple(y)
print(mytuple)
mytuple = ("mango","kiwi")
y=("orange",)
mytuple +=y
print(mytuple)
mytuple = ("mango","kiwi","straberry","grapes")
y =list(mytuple)
y.remove("mango")
mytuple=tuple(y)
print(mytuple)
fruits = ("cherry", "strawberry", "raspberry")
(green,orange,red)=fruits
print(green)
print(orange)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,orange,*red)=fruits
print(green)
print(orange)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,*orange,red)=fruits
print(green)
print(orange)
print(red)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 3
print(mytuple)
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"1","2","3","4","5","1","2"}
print(thisset)
for x in thisset:
    print(x)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
set1 = {"a", "b" , "c","a","b"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana"}
x.intersection_update(y)
print(x)
x = {"orange","kiwi","apple","banana"}
y = {"grapes","banana","kiwi"}
z = x.intersection(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft","apple","pineappple"}
z= x.symmetric_difference(y)
print(z)
thisdict = {
    "brand" : "ford",
    "model" : "hyundei",
    "year" : 1965
}
print(thisdict)
thisdict = {
    "Brand" : "hero",
    "Model" : "splender",
    "Year" : 1950
}
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("model"))
print(thisdict["year"])
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)
car["colour"] = "red"
print (x)
mobile = {
    "company" : "realme",
    "model" : "7 pro",
    "year" : 2020
}
x = mobile.values()
print(x)
mobile["colour"] = "white"
print(x)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
thisdict =	{
  "brand": "KIA",
  "model": "nexon",
  "year": 2005
}
thisdict.update({"year": 2006})
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"]
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
    print(x)
for x in thisdict:
    print(x)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print("yes") if a < b else print(" no")
a = 2
b = 330
print("A") if a > b else print("B")
i = 1
while i < 6 :
    print (i)
    i +=1
i = 6
while i > 1:
    print (i)
    i -=1
i = 1
while i < 6:
    print(i)
    if i ==3:
     break
    i +=1
i = 0
while i < 8 :
    i +=1
    if i ==4:
        continue
    print(i)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj :
    for y  in fruits:
        print(x,y)
x = "awesome"
def myfunc():
    x = "fantastic"
    print("python is "+x)

myfunc()
print("python is "+ x)
import random
print(random.randrange(1,9))
txt = "today is my 1st day in job"
x = txt.capitalize()
print(x)
x = txt.casefold()
print(x)
txt = "pavan"
y = txt.center(20,"*")
print(y)
txt = "today is my first day in job"
z = txt.count("job", 1, 10)
print(z)
txt = "my name is kålyan"
x = txt.encode()
print(x)
txt = "my name is kalyan."
x = txt.endswith(".")
print(x)
txt = "m\ty n\tam\te i\ts kålyan"
x = txt.expandtabs(4)
print(x)
txt = "my name is kalyan"
x = txt.find("s",1,10)
print(x)
txt = "my name is kålyan"
x = txt.index("e")
print(x)
txt = "my name is pavan, my age is {}"
x = txt.format(22)
print(x)
txt = {"x": "ford","y": "mustung"}
z = ('{y} is one of the model of {x}'.format_map(txt))
print(z)
txt= "pavan06"
x = txt.isalnum()
print(x)
x = txt.isalpha()
print(x)
txt = "123"
x = txt.isdecimal()
print(x)
txt = "demo 456"
x = txt.isidentifier()
print(x)
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
txt = "boys are playing cricket"
x = txt.isspace()
print(x)
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello8989"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
txt = "banana"
x = txt.ljust(8,"*")
print(x)
x = txt.center(10,"@")
print(x)
txt = "       college          is beautiful    "
x = txt.lstrip()
print(x)
txt = {"x":'john',"y":'wick'}
z = ("{x}'s last name is {y}".format_map(txt))
print(z)
txt = {"x": 'geeks for geeks',"y": 'app'}
z = ('{x},{y}'.format_map(txt))
print(z)






from airflow import DAG

dag_default_config = {
    "Start_date":datetime(2016,1,1),
    "owner":"airflow"
}

dag_object =DAG('my_dag',dag_default_config = dag_default_config,description="Sample DAG",schedule_interval="0 12 * * *")

























# Press the green button in the gutter to run the script.






# See PyCharm help at https://www.jetbrains.com/help/pycharm/