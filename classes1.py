class circle(object):
    pi = 3.14
    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return (self.radius**2) * circle.pi
    
    def cir(self):
        return (self.radius*2)*circle.pi

       
