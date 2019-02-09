class person(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hobby(self):
         print('hobby is programming')

class emp(person):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hobby(self):
        print('hobby is coding')

    def branch(self):
        print('branch is software engg')

     

    
