#examples of genrators 

def gensquare(N):
    for x in range(N):
        yield x**2

       
s = 'hello'
s_iter = iter(s)
