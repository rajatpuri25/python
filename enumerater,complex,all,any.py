Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>   l = [a,b,c,d,e,f]
  
SyntaxError: unexpected indent
>>> l = [a,b,c,d,e,f]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    l = [a,b,c,d,e,f]
NameError: name 'a' is not defined
>>> l = ['a','b','c','d','e','f']
>>> for count,item in enumerate(l)
SyntaxError: invalid syntax
>>> for count,item in enumerate(l):
	print(count)
	print(item)

	
0
a
1
b
2
c
3
d
4
e
5
f
>>> for count,item in enumerate(l):
	if count>3:
		break
	else:
		print(count)
		print(item)

		
0
a
1
b
2
c
3
d
>>> l = [true,true,false]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l = [true,true,false]
NameError: name 'true' is not defined
>>> l = ['true','true','false']
>>> any(l)
True
>>> all(t)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    all(t)
NameError: name 't' is not defined
>>> all(l)
True
>>> m = [True,False,True]
>>> all(m)
False
>>> any(m)
True
>>> complex(12,)
(12+0j)
>>> complex(1+2j)
(1+2j)
>>> complex(1,9)
(1+9j)
>>> 
