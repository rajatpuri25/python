""" prime number """

def prime(num):
    for n in range(2,num):
        if num%n==0:
            print("not prime")
            break
    else:
        print("prime")
