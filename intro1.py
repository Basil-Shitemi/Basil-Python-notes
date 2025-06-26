#str
print('Hello World')
name = input('what is your name?')
print('Hello ' + name)

#fundamental data types
## int and float
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(4 / 2)
print(type(2 / 4))
print(4 // 2)
print(type(4 // 2))
print(type(2 + 4))
print(type(2.1 + 4))
print(6 % 4)
print(2**3)

#math functions(Google python3 math functions)
print(round(3.1))
print(abs(-20))
#Operator precedence(obeys BODMAS)
print(20-3*4)
print(bin(5))
print(int('0b101', 2))

#variables
user_iq=190
print(user_iq)
user_age =user_iq/4
print(user_age)
a=user_age
print(a)
#constants
PI=3.14
#dunder variables(should not be changed)
#others
a,b,c=1,2,3
print(a)
print(b)
print(c)

#expressions and statements
#augmented assignment operator
some_values=5
some_values+=2
print(some_values)
some_values*=2
print(some_values)
#some_values-=2 is same as some_values=some_values-2
     #strings
print(type('Hello world 2025!'))
username='supercoder'
password='supersecret'
long_string= '''
WOW
0 0
---
'''
print(long_string)

first_name= 'Basil'
second_name= 'Shitemi'
full_name= first_name+' ' +second_name
print(full_name)
#string concatenation(adding strings together)
print('Hello' + ' ' + 'World')
#Type conversion
print(type(str(100)))
print(type(int(str(100))))
#means;a=str(100), b=int(a), c=type(b)

#Escape Sequence(using backslash\, new tab and new line)
weather= "\t It\'s \"kind of\" sunny. \n Have a good day!"
print(weather)
##Formatted strings(f) for python 3, .format for python 2&3-complex
name= 'Basil'
Age= 26

print('Hello '+(name) + ' You are ' + str(Age) + ' years old')
print(f'Hello {name} You are {Age} years old' )
#string indexes.
selfless='me me me'
selfish='01234567'
print(selfish[0])
#[start:stop:stepover]
print(selfish[0:8:2])
print(selfish[-1])
print(selfish[: :-2])
print(selfish[-2: :])
  #Immutability(strings are immutable, cannot be changed unless you create sth new)
selfish='01234567'
selfish=selfish + '8'
print(selfish)# something new created.

#Built in Functions(len,int,print,type, float,abs, round etc) and string Methods(eg .format, .upper, .capitalize, .find, .replace)
greet='hellooww'
print(len(greet))
#string methods
quote='to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be','me'))
print(quote)
quote=quote+ ' ' + 'OK'
print(quote)
#Booleans(bool)
name= 'Basil'
is_cool=False
is_cool=True
print(bool(1))
print(bool(0))
print(bool(True))

#Type conversion
date_of_birth= int(input('when were you born?'))
current_date= 2025
age= current_date-date_of_birth
print(f'You are {age} years old')
#Ensure appropriate commenting of your code.
#Exercise
username=input('what is your name')
password=input('what is your password')
password_lenght=len(password)
hidden_password=password.replace(password,'*' * password_lenght)
print(f'Hello {username} your password {hidden_password} is {password_lenght} characters long')
#list
li=[1,2,3,4,5]
li2=['a','b','c']
li3=[1,2.5,'a',True]
#Data structure
amazon_cart=['notebooks','sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])
#list slicing
amazon_cart=[
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])
##list are mutable
amazon_cart[0]='laptop'
print(amazon_cart[0:3])
amazon_cart[1]='gum'
print(amazon_cart)
new_cart=amazon_cart #replacing the list
new_cart[0]='biscuits'
print(new_cart)
print(amazon_cart)
#note(how to correct above)
amazon_cart[0]='laptop'
new_cart=amazon_cart[:] #copying the list
new_cart[0]='biscuits'
print(new_cart)
print(amazon_cart)
#matrix;multiple dimensional list-for ml imaging.
matrix=[
[1,2,3],
[2,4,6],
[7,8,9]
]
print(matrix[0][1])

#list methods-changes/modifies the list in place
basket=[1,2,3,4,5]
print(len(basket))

#adding
new_list=basket.append(100)#changes the list in place
new_list=basket.insert(4,44)
new_list=basket.extend([100,101])
#removing
new_list=basket.pop(1)
new_list=basket.pop()
new_list=basket.remove(4)
new_list=basket.clear()

print(basket)
print(new_list)
new_list=basket
print(basket)
print(new_list)
basket=['a','b','c','x','d','e','d']
print(basket.index('b'))
print(basket.index('b',0,2))
print('d'in basket)
print('yo' in 'hi my name is')
print(basket.count('d'))
basket.sort()
print(basket)
print(sorted(basket))#does not modify the list in place
new_basket=basket.copy()
print(basket)
print(new_basket)
basket.sort()
basket.reverse()
print(basket)
print(basket[::-1])
print(list(range(1,100)))
print(list(range(100)))
sentence='!' #or =' '
new_sentence=sentence.join(['Hi','my','name', 'is','Boil'])
print(new_sentence)
#List unpacking
a,b,c,*other,d,e=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(other)
print(d)
print(e)
##none-data type that represents the absence of value.
weapons=None
print(weapons)