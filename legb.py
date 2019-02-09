""" local enclosing local enclosing local ,global,builtin (legb)"""
name = 'rajat puri'# global
def greet():
    name = 'rajat' #local
    def hello():
        print("hello"+name) #enclosing local

    hello()

greet()       
len(hello())  #builtin  
