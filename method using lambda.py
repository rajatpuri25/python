Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Acer/AppData/Local/Programs/Python/Python36-32/function.py 
>>> 2
2
>>> 5
5
>>> 
 RESTART: C:/Users/Acer/AppData/Local/Programs/Python/Python36-32/function.py 
>>> prime(13)
prime
>>> prime(4)
not prime
>>> even = lambda num: num %2 == 0
>>> even(2)
True
>>> even(7)
False
>>> addd=lambda x,y:x+y
>>> addd(2,4)
6
>>> s=lambda s:s[0]
>>> s['hello']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s['hello']
TypeError: 'function' object is not subscriptable
>>> s('hello')
'h'
>>> st=lambda st:st[::-1]
>>> st('puri')
'irup'
>>> st.reverse('sd')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    st.reverse('sd')
AttributeError: 'function' object has no attribute 'reverse'
>>> 
