#function
def pal_string(a):
    a=str(input('Enter  string'))
    b=reversed(a)
    if(a==b):
        print('palindrome')
    else:
        print('not a palindrome')
