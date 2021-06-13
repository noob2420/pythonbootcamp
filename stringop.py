Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #print string
>>> print('30 days 30 hours')
30 days 30 hours
>>> #assigning string to variables
>>> v='Taj mahal'
>>> print(v)
Taj mahal
>>> 
>>> #indexing string
>>> x='Eiffel tower'
>>> print(x[2])
f
>>> print(x[4])
e
>>> #to print characters from string
>>> s='Puneeth'
>>> print(s[2:6])
neet
>>> 
>>> #converting upper case and lowercase
>>> d='
SyntaxError: EOL while scanning string literal
>>> d='colosseum'
>>> print(d.upper())
COLOSSEUM
>>> print(d.lower())
colosseum
>>> 
>>> #string concat
>>> m='yamaha'
>>> n='r7'
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(a+b)
NameError: name 'a' is not defined
>>> print(m+n)
yamahar7
>>> 
>>> #casefold() use
>>> b='The BEst SUPER biKe'
>>> b=text.casefold()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b=text.casefold()
NameError: name 'text' is not defined
>>> c=b.textfold()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c=b.textfold()
AttributeError: 'str' object has no attribute 'textfold'
>>> c=b.casefold()
>>> 
>>> g="SHE SELLS SEA SHELLS ON THE SEA SHORE"
>>> print(g.capitalize())
She sells sea shells on the sea shore
>>> print(g.title())
She Sells Sea Shells On The Sea Shore
>>> print(g.swapcase())
she sells sea shells on the sea shore
>>> 
>>> #to check the type of characters present in the string
>>> i='She SELLS sea shells on the SEA shore'
>>> print(i.isalpha())
False
>>> print(i.isalnum())
False
>>> print(i.isdigit())
False
>>> print(i.islower())
False
>>> print(i.isupper())
False
>>> 