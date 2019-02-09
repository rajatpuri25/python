a=int(input('Enter a number '))
temp=a
rev=0
while(a>0):
    d=a%10
    rev=rev*10+d
    a=a//10
if(temp==rev):
    print('palindrome')
else:
    print('not a palindrome')
    
    
