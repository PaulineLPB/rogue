import math

class Coord(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __eq__(self,other):
        if not isinstance(other,Coord):
            return False
        if self.x==other.x and self.y==other.y:
            return True
        return False
        
    def __repr__(self):
        return f"<{self.x},{self.y}>"
        
    def __add__(self,other):
        return Coord(self.x+other.x,self.y+other.y)
        
    def __sub__(self, other):
        a=self.x-other.x
        b=self.y-other.y
        return Coord(a,b)
        
    def distance(self, other):
        return math.sqrt(math.pow(other.x-self.x,2)+math.pow(other.y-self.y,2))
        
    def direction(self, other):     #indique la direction depuis self vers other
        d=self-other
        cos=d.x/self.distance(other)
        if cos > 1/math.sqrt(2):
            return Coord(-1,0)
        if cos < -1/math.sqrt(2):
            return Coord(1,0)
        if d.y>0:
            return Coord(0,-1)
        else:
            return Coord(0,1)
