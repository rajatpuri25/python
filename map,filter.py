Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = [47,11,42,13]
>>> reduce(lambda x,y:x+y,l)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    reduce(lambda x,y:x+y,l)
NameError: name 'reduce' is not defined
>>> map(lambda x,y:x+y,l)
<map object at 0x03A295D0>
>>> print(map(lambda x,y:x+y,l))
<map object at 0x03A29550>
>>> print([list(map(lambda x,y:x+y,l))])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print([list(map(lambda x,y:x+y,l))])
TypeError: <lambda>() missing 1 required positional argument: 'y'
>>> l = [47,11,42,13]
>>> m = [1,35,54,54]
>>> print([list(map(lambda x,y:x+y,l,m))])
[[48, 46, 96, 67]]
>>> print(map(lambda x,y:x+y,l,m))
<map object at 0x03A29BD0>
>>> print(list(map(lambda x,y:x+y,l,m)))
[48, 46, 96, 67]
>>> temp = [0,32,100]
>>> print(list(lambda t:(9.0/5)*32+5,temp))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(list(lambda t:(9.0/5)*32+5,temp))
TypeError: list() takes at most 1 argument (2 given)
>>> print(list(map(lambda t:(9.0/5)*32+5,temp)))
[62.6, 62.6, 62.6]
>>> print(list(map(lambda t:(9/5.0)*32 + 5,temp)))
[62.6, 62.6, 62.6]
>>> print(list(map(lambda t:(9.0/5)*t+32,temp)))
[32.0, 89.6, 212.0]
>>> print(list(reduce(lambda t:(9.0/5)*t+32,temp)))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(list(reduce(lambda t:(9.0/5)*t+32,temp)))
NameError: name 'reduce' is not defined
>>> print(list(filter(lambda t:(9.0/5)*t+32,temp)))
[0, 32, 100]
>>> print(list(filter(lambda n:n%2==0,l)))
[42]
>>> print(list(filter(lambda n:n>1,m)))
[35, 54, 54]
>>> print(list(map(lambda n:n>1,m)))
[False, True, True, True]
>>> 
