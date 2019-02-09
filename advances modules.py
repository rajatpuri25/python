Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from colections import counter
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from colections import counter
ModuleNotFoundError: No module named 'colections'
>>> from collections import counter
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from collections import counter
ImportError: cannot import name 'counter'
>>> from collections import ounter
KeyboardInterrupt
>>> from collections import Counter
>>> l = [1,1,1,1,1,2,2,2,2,2,3,3,3,,4,4,4,4]
SyntaxError: invalid syntax
>>> l = [1,1,1,1,1,2,2,2,2,3,3,4,4,4]
>>> counter(l)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    counter(l)
NameError: name 'counter' is not defined
>>> 
KeyboardInterrupt
>>> Counter(l)
Counter({1: 5, 2: 4, 4: 3, 3: 2})
>>> s = 'asdfgjmjhghfdsaaaaaaaaaaaaaaasadsfdfggv'
>>> Counter(s)
Counter({'a': 17, 's': 4, 'd': 4, 'f': 4, 'g': 4, 'j': 2, 'h': 2, 'm': 1, 'v': 1})
>>> a = 'gagan is my best friend'
>>> word = a.split()
>>> Counter(word)
Counter({'gagan': 1, 'is': 1, 'my': 1, 'best': 1, 'friend': 1})
>>> b = 'rama is is is is is my my best friend'
>>> word = b.split()
>>> Counter(word)
Counter({'is': 5, 'my': 2, 'rama': 1, 'best': 1, 'friend': 1})
>>> most_common(words)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    most_common(words)
NameError: name 'most_common' is not defined
>>> c = 
KeyboardInterrupt
>>> c = Counter(word)
>>> c.most_common(2)
[('is', 5), ('my', 2)]
>>> c.list(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c.list(c)
AttributeError: 'Counter' object has no attribute 'list'
>>> list(c)
['rama', 'is', 'my', 'best', 'friend']
>>> set(c)
{'rama', 'is', 'my', 'friend', 'best'}
>>> dict(c)
{'rama': 1, 'is': 5, 'my': 2, 'best': 1, 'friend': 1}
>>> c.items()
dict_items([('rama', 1), ('is', 5), ('my', 2), ('best', 1), ('friend', 1)])
>>> c+=Counter()
>>> c.most_counter(:-5-1:-1)
SyntaxError: invalid syntax
>>>  c.most_counter(-4,-1)
 
SyntaxError: unexpected indent
>>> c.most_counter(-5,-1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c.most_counter(-5,-1)
AttributeError: 'Counter' object has no attribute 'most_counter'
>>>  c.most_counter(-4:-1)
 
SyntaxError: unexpected indent
>>> c.most_counter(-4:-1)
SyntaxError: invalid syntax
>>> c.most_counter(-4,-1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.most_counter(-4,-1)
AttributeError: 'Counter' object has no attribute 'most_counter'
>>> 
