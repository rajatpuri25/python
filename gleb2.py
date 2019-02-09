#local variable
x=50
def func(x):
	x=2
	print(x)

func(x)
print('x is still',x)

#global variable
y=50
def func(x):
    global y
    print(y)
    y=2
    print(y)

func(y)
print('y is ',y)
