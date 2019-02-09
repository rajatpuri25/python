
#exception2

def askint():
    
  while True:  
    try:
        val = int(input('please enter the integer'))
    except:
        print('doesnot enter integer')
        continue
    else:
        print('correct,i.e integer')
        break
    finally:
        print('Finally block executed')
    print (val)
