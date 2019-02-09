#exception examples
 #1

for i in ['a','b','c']:
    try:
        for i in ['a','b','c']:
          print (i**2)
    except:
        print('error in printing')
    finally:
        print('finally block executed')
#2

x = 5
y = 0
try:
    z=x/y
except:
    print("division by zero error")
finally:
    print('all done')

 #3
def askint():
 while True:  
    try:
        val = int(input('please enter the integer'))
        sq = val**2
        print('squareof a number is',sq)
    except:
        print('doesnot enter integer')
        continue
    else:
        print('correct,i.e integer')
        break
    finally:
        print('Finally block executed')

    
