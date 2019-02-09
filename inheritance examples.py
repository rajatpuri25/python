class line(object):

    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2

    def slope(self):
         x1,y1=self.coor1
         x2,y2=self.coor2
         print("slope is",(y2-y1)/(x2-x1))
         
           
         
