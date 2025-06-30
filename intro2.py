#Dictionary(dict)-is unordered collection of data items.
dictionary={
  'a':[1,2,3],
  'b':'hello',
  'x':True
}
print(dictionary['a'][1])

my_list=[{
  'a':[1,2,3],
'b':'hello',
'x':True
},
{
  'a':[4,5,6],
'b':'hello',
'x':True 
}]
print(my_list[1]['a'][2])
#understanding data structures(eg list,dict) Use list when order is important and dict when not & there are more/different entries.
#Dictonary keys-keys in dictionary should be immutabl(Can't be changed ) & shoul be unique,exists once. List can not be used as key.
dictionary={
  123:[1,2,3],
  123:'yes',
  True:'hello',
 'x':True
}
print(dictionary[123])
#Dictionary methods
user={
 'basket':[1,2,3],
  'greet':'hello',
  'age':22
}

print(user['greet'])
print(user.get('age'))
print(user.get('age',55))
user2=dict(name='john',age=55)
print(user2)
print('basket'in user)
print('hello' in user.keys())
print('hello' in user.values())
print(user.items())#returns a tuple
user2=user.copy()
#print(user.clear())
print(user.pop('greet'))
print(user.popitem())
print(user.update({'age':55}))
print(user)

#Tuples-immutable lists
my_tuple=(1,2,3,4,5,5)
print(my_tuple[1])
print(5 in my_tuple)
new_tuple=my_tuple[1:4]
print(new_tuple)
x,y,z,*other=(1,2,3,4,5)
print(y)
#Tuple methods; count and index.
print(my_tuple.count(5))
print(my_tuple.index(4))
print(len(my_tuple))
#Sets-unordered collection of unique objects)
my_set={1,2,3,4,5,5}
print(my_set)
my_list=[1,2,3,4,5,5]
print(set(my_list))
#print(my.set[0]) #error-set does not support indexing
print(1 in my_set)
print(len(my_set))
print(list(my_set))
my_set2=my_set.copy()
my_set.clear()
print(my_set2)
print(my_set)
#other set methods
my_set={1,2,3,4,5}
your_set={4,5,6,7,8,9,10}
print(my_set.difference(your_set))
print(my_set.discard(5))
print(my_set)
print(my_set.difference_update(your_set))
print(my_set)
print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))#Have nothing in common or not
print(my_set.union(your_set))# print(my_set|your_set)
print(my_set.issubset(your_set))#is my_set a portion of your_set,true/false
print(my_set.issuperset(your_set))# is my_set a superset of ypur_set, true?false
#N/B- Always use python notes/online for methods and functions references.

#conditional logic
is_old=False
is_licenced= False
if is_old:
  print('You are old enough to drive!')
elif is_licenced: #can appear severally
  print('You can drive now!')
else:
  print('You are not of age and not licenced!')
if is_old and is_licenced:
  print('You are old enough to drive and you have a licence!')
else:
  print('You are not of age and not liicenced!')
print('okokok')
#Identation in Python- unlike Javascript, here it is well indented,and ideally should be 4 spaces.
#Truthy and Falsy- involves machine automatic conversion of values to boolean. Examples of Falsy are 0,none,{},[],(),'',set(),range(0) etc
username=''
password='123'
if username and password:
  print('You can enter')
else:
  print('You cannot enter')
#Ternary Operator- shortcut for if else statement..condition_if_true if condition else condition_if_false
is_friend=False
can_message='message allowed' if is_friend else 'not allowed to message'
print(can_message)
#Short Circuiting- when we use 'or' and 'and' in a condition,it 'short circuits and stops evaluating once if finds the first adequate condition.
is_friend=True
is_user=True
if is_friend or is_user:
  print('Best friend forever')
  if is_friend and is_user:
    print('wow')
#logical operators- and, or, <,>,==,!=,<=,>=,not
#eg 'a'<'b,'a'<'A', 'a'>'Hello' here python uses the unicode values that are assigned to each character. If it is a word, the first letter is considered and compared based on their unicode values.like for 'a' is 98 and 'A' is 65.
print(not(True))#gives the opposite of the booolean result found.
print('a'>'A')
print('a'<'hello')
print('a'>'b')
print(1<2<3<4)
print(1<2>3<4)
print(1<=0)
print(1==1)#equals
print(2!=3)# != means not equal to
is_magician=False
is_expert=True
if is_expert and is_magician:
  print('You are a master magican')
elif is_magician and not is_expert:
  print('Atleast you are getting there')
elif not is_magician:
  print('You need magic powers')
# == checks for equality of value, whereas 'is' checks if the location in memory where the value is stored is the same.
print(True is 1)
print(1 is 1)
print([] is [])#each new list is created in a new location in memory,
print('1' is '1')

print(10 is 10.0)
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a==b)

# for loops ie for variable in iterable:
for item in 'zero to mastery':
  print(item)
for item in [1,2,3,4,5]:#list
  print(item)
for item in {1,2,3,4,5}:#set
  print(item)
for item in (1,2,3,4,5):#tuple
  print(item)
  print(item)
  print(item)
print(item)
for item in (1,2,3,4,5):
  for x in ['a','b','c']: #nested loops
    print(item,x)
#Iterables-is an object or collection that can be iterated over.-list, dictionary,tuple,set,string
#for item in 50: print(item) error, cause 50 is an int hence not iterable
# as for dictionary
user={
  'name': 'Golem',
  'age':50,
  'can_swim': False
}
for item in user:
  print(item)
for items in user.items():
  print(items)
for items in user.keys():
  print(items)
for items in user.values():
  print(items)
for key,value in user.items():
  print(key,value)
#Exercise-tricky counter
my_list=[1,2,3,4,5,6,7,8,9,10]
counter=0
for items in my_list:
  counter=counter+items
print(counter)
print(sum(my_list))
#range()
for number in range(0,100):
  print(number)
for items in range(0,10):
  print('email list')
for _ in range(0,10,2):
  print(_)
for _ in range (10,0,-2):
  print(_)
for _ in range(2):
  print(list(range(10)))
#enumerate()
for i, character in enumerate('hello'):
   print(i,character)
for i,char in enumerate([1,2,3,4]):#even tuples
  print(i,char)
for i, char in enumerate(list(range(100))):
  if char==50:
    print(f' index of 50 is:{i}')
#white loops
# i-0
# while i <50:
  #print(i)#infinite loop. to stop, break the loop.
i=0
while i<50: 
  print(i)
  i=i+1#or i+=1
  break#else statement does not print when you use break.
else:
  print('Done with all the work')

my_list=[1,2,3]
for items in my_list:
  print(items)

i=0
while i < len(my_list):
  print(my_list[i])
  i+=1

while True :
  response=input('say something:')
  if response== 'bye':
    break
##break,continue,pass
my_list=[1,2,3]
for items in my_list:
  print (items)
  continue
i=0
while i< len(my_list):
  print(my_list[i])
  i+=1
  continue#continue goes back to the loop. break goes out of the loop. pass does nothing, it assumes the previous line.  

##Exercise
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]  
]
 ##iterate over picture
#if 0 print ' '
#if 1 print *

for row in picture:
  for pixel in row:
    if (pixel == 1):
      print('*',end='')
    else:
      print(' ',end='')
  print('')
  #good code is clean,readable,predictable, DRY(don't repeat yourself)
#Exercise-check for duplicates in a list.
some_list=['a','b','c','b','d','m','n','n']
duplicates=[]
for value in some_list:
  if some_list.count(value)>1:
    if value not in duplicates:
      duplicates.append(value)
print(duplicates)
#Functions-we can create our own functions. Ensure DRY, use def to create a functon.
def say_hello():
  print('hello')

say_hello()
say_hello()# Able to call the function multiple times.
##Arguements vs parameters.
   #parameters-define the function.
def say_hello(name, emoji):
  print(f'hello {name} {emoji}')

  ##Arguements-used when we call/invoke the function ie the specific name and emoji
say_hello('Basil', '馃槉')
say_hello('Dan', '馃槉')
#positional Arguements-position matters, should be the  same position as the parammeter.
#keyword Arguements-not worry about position. Better stick to the parameter name.
def say_hello(name='Biko',emoji='馃槉'):
  print(f'Hello {name} {emoji}')
say_hello(name='Basil',emoji='馃槉')
say_hello()
say_hello('Timmy')
#return-use to exit the function.A function either modifies something or returns something.
def sam (num1,num2):
  #print('Hi')
  return num1+num2
print(sam(10,5))
total=sam(10,5)
print(sam(10,total))
##or 
print(sam(10,sam(10,5)))

def sam(num1,num2):
  def another_func(n1,n2):
    return n1+n2
  return another_func(num1,num2)#return exits the function.
total=sam(10,20)
print(total)
#Exercise-Tesla

#Methods vs functions. methods use dot notation.
##inbuilt functions include; input, list, print, max, min etc. created function starts with def.Every datatype has its own methods.
#Docstrings-allows us to comment inside of our function.
def test(a):
  '''
  Info: this function tests and prints param a
  ''' ##docstring,comment on function's work.
  print(a)
test('!!!')
#help(test)
print(test.__doc__)
#Clean code
def is_even(num):
  if num%2==0:
    return True
  else:
    return False

print(is_even(51))
#cleaning the code above:
def is_even(num):
  return num%2==0

print(is_even(51))
#args and kwargs(Arguements and Keywords arguements),
# *args ***kwargs-allows us to grab any number of arguements.
#Rule:params eg name,*args eg 2,default parameters eg i='HI',**kwargs eg num1=4.
def super_func(*args,**kwargs):
  total = 0
  for item in kwargs.values():
      total += item
  return sum(args) + total

print(super_func(1,2,3,4,5,num1=5,num2=10))
#Exercise-Highest Even.
def highest_even(li):
  evens=[]
  for items in li:
    if items%2==0:
      evens.append(items)
  return max(evens)#loop through then return

print(highest_even([10,2,3,4,8,11]))
##scope-what variables do I have access to? 'like a new world' "it is not defined"
#function scope- if function is defined inside a function, it is not accesible outside the function eg after def.Global scope-anything we define outside of a function. eg total=100. Scope rules covered, ie everything in their respective universe.Scope rules: 1-start with local scope. 2-parent local scope. 3-global scope-ie no indentation. 4-built in python functions.
#Global keyword-used to access global variables.
total=0
def count():
  global total#may be confusing.
  total+=1
  return total

count()
count()
print(count())
#dependency injection-instead of accesing global variables, we can use this.
total=0
def count(total):
  total+=1
  return total

print(count(count(count(total))))
#nonlocal keyword-used to refer to parent local.nonlocal is  a new keyword in python3.
def outer():
  x='local'
  def inner():
    nonlocal x#reasigns it to be 'nonlocal'
    x='nonlocal'
    print('inner:',x)

  inner()
  print('outer:',x)

outer()
#why do we need scope?- to save memory and ensure our program runs smoothly.

#Pure functions-rules, given the same input, it will always return the same output. second rule, it should not return any side efects ie don't interact with the outside world. Keep functions and data separate. eg map, reduse, filter,zip(Function,data)
def multiply_by2(li):
  new_list=[]
  for items in li:
    new_list.append(items*2)

  return new_list

print(multiply_by2([1,2,3]))
#map, filter,zip, reduce.
#map
my_list=[1,2,3]
def multiply_by2(item):
  return item*2

print(list(map(multiply_by2, my_list)))
print(my_list)#does not change the original list, no Side effects.No effects on outside world.
#filter.
my_list=[1,2,3]
def only_odd(item):
  return item%2!=0

print(list(filter(only_odd,my_list)))
print(my_list)
#zip- like a zipper,takes two iterables and zips them together, comes up with a tuple.- even more than two iterables.
my_list=[1,2,3]
your_list=(10,20,30)
other_list=[5,4,3]

print(list(zip(my_list, your_list,other_list)))#create new tuple.
#Reduce
from functools import reduce #have to import reduce.
my_list=[1,2,3]
def accumulator(acc, item):
  print(acc,item)
  return acc+item

print(reduce(accumulator,my_list,0)) 
print(my_list)
#comprehensions. used with list,set, dictionaries.
my_list=[]
for char in 'hello':
  my_list.append(char)

print(my_list)
#better way, using Comprehensions instead. (parameter for parameter in iterables)
my_list=[char for char in 'hello']
print(my_list)
my_list2=[num for num in range(0,100)]
print(my_list2)
my_list3=[num**2 for num in range(0,100)]
print(my_list3)
my_list4=[num**2 for num in range(0,100) if num%2==0]
print(my_list4)
#set comprehensions.- change the [] in list to {} and do the same comprehensions.
#Dictionary comprehensions.
simple_dict={
  'a':1,
  'b':2
}
my_dict={key:value**2 for key,value in simple_dict.items() if value%2==0}# makes the code less readable.
print(my_dict)
my_dict={num:num*2 for num in [1,2,3]}
print(my_dict)
#Exercise-comprehension. duplicates
some_list=['a','b','c','b','d','m','n','n']

duplicates=list(set([x for x in some_list if some_list.count(x)>1]))
print(duplicates)

#How to organize code- in python files and using functions.
#we use modules ie combine .py file into a package.
#how to use code from another module; just type import and the name of the module.eg in main.py,import utility.The utility.py file is imported and another file generated(__pycache__) it loads up another file utility.cpython-cpython as the interpreter. You can import as many modules as you want.
#pycharm (an IDE)-can create a package and a module.
#package-a folder that contains modules. How to import a module in a package; import package.module. eg shopping.shopping_cart.Still, a _pycache_file is created for this module.
##package in Pycharm- create a package and a module. Then import package.module.Packages in pycharm has __init__.py
#import utility
##import shopping.more_shopping.shopping_cart (then print the same) or
# from shopping.more_shopping.shopping_cart import buy
# print(buy('apple'))
# from utility import multiply,divide
# print(divide(5,2))
##from shopping.more_shopping import shopping_cart- in the case of existing functions.