Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'i'am'
SyntaxError: invalid syntax
>>> 'i'm dfsdf'
SyntaxError: invalid syntax
>>> "i'm dsasx"
"i'm dsasx"
>>> len("dsdsf")
5
>>> s="dsdsd"
>>> s
'dsdsd'
>>> print s
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(s)?
>>> print"s"
SyntaxError: invalid syntax
>>> print s
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(s)?
>>> print 's'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('s')?
>>> print s
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(s)?
>>> print 'first:{x} second:{y} third:{x} '.format(x="rajat",y="puri")
SyntaxError: invalid syntax
>>> print 'first: {x} second: {y} third: {x} '.format(x='rajat',y='puri')
SyntaxError: invalid syntax
>>> print("hello')
      
SyntaxError: EOL while scanning string literal
>>> SyntaxError: EOL while scanning string literal
SyntaxError: invalid syntax
>>> 
>>> print("hello")
hello
>>> from__future__import print_function
SyntaxError: invalid syntax
>>> from __future__ import print_function
>>>  print 'first: {x} second: {y} third: {x} '.format(x='rajat',y='puri')
 
SyntaxError: unexpected indent
>>>  print ('first: {x} second: {y} third: {x} '.format(x='rajat',y='puri'))
 
SyntaxError: unexpected indent
>>>  print'first: {x} second: {y} third: {x} '.format(x='rajat',y='puri')
 
SyntaxError: unexpected indent
>>>  print('first: {x} second: {y} third: {x} '.format(x='rajat',y='puri'))
 
SyntaxError: unexpected indent
>>> print('one: {x}'.format(x='rajat'))
one: rajat
>>> x=[1,2,3,4]
>>> x
[1, 2, 3, 4]
>>> x.append(5)
>>> x
[1, 2, 3, 4, 5]
>>> x.pop()
5
>>> x
[1, 2, 3, 4]
>>> x.pop(3)
4
>>> x
[1, 2, 3]
>>> x=x.pop(0)
>>> x
1
>>> x
1
>>> l=[2,3,4,5]
>>> x = l.pop(1)
>>> l
[2, 4, 5]
>>> l1=[1,2,3]
>>> l2=[6,4,5]
>>> l3=[1,5,2]
>>> matrix=[l1,l2,l3]
>>> matrix
[[1, 2, 3], [6, 4, 5], [1, 5, 2]]
>>> matrix[0]
[1, 2, 3]
>>> matrx[1]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    matrx[1]
NameError: name 'matrx' is not defined
>>> matrix[1]
[6, 4, 5]
>>> matrix[3]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    matrix[3]
IndexError: list index out of range
>>> matrix[0][2]
3
>>> matrix[1][1]
4
>>> matrix[2][0]
1
>>> absd=[l1,l2,l3]
>>> absd
[[1, 2, 3], [6, 4, 5], [1, 5, 2]]
>>> first_col = [row[0] for row in matrix]
>>> first_col
[1, 6, 1]
>>> first_col = [row[1] for row in matrix]
>>> first_col
[2, 4, 5]
>>> dictionaries
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dictionaries
NameError: name 'dictionaries' is not defined
>>> my_dict = {'k1':'ram','k2':2.2,'k3':2}
>>> k1
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    k1
NameError: name 'k1' is not defined
>>> my_dict['k1']
'ram'
>>> my_dict['k2']
2.2
>>> my_dict['k3']
2
>>> my_dict['k1'][0]
'r'
>>> my_dict['k1'].upper()
'RAM'
>>> my_dict['k1'][::-1]
'mar'
>>> my_dict['k1'][:2:]
'ra'
>>> my_dict['k1'][::2]
'rm'
>>> my_dict['k3']+2
4
>>> my_dict[k4]='qwert'
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    my_dict[k4]='qwert'
NameError: name 'k4' is not defined
>>> my_dict['k4']='qwert'
>>> my_dict['k5']='12w'
>>> my_dict
{'k1': 'ram', 'k2': 2.2, 'k3': 2, 'k4': 'qwert', 'k5': '12w'}
>>> d={'k1'={'ram':{'age':42}}}
SyntaxError: invalid syntax
>>> d={'k1':{'ram':{'age':42}}}
>>> d['k1']['ram']['age'].upper()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d['k1']['ram']['age'].upper()
AttributeError: 'int' object has no attribute 'upper'
>>> d['k1']['ram']['age']
42
>>> my_dict.key()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    my_dict.key()
AttributeError: 'dict' object has no attribute 'key'
>>> my_dict.keys()
dict_keys(['k1', 'k2', 'k3', 'k4', 'k5'])
>>> my_dict.values()
dict_values(['ram', 2.2, 2, 'qwert', '12w'])
>>> my_dict.items()
dict_items([('k1', 'ram'), ('k2', 2.2), ('k3', 2), ('k4', 'qwert'), ('k5', '12w')])
>>> my_dict
{'k1': 'ram', 'k2': 2.2, 'k3': 2, 'k4': 'qwert', 'k5': '12w'}
>>> print tupple
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(tupple)?
>>> print ("tupple")
tupple
>>> 
