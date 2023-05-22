from Coord import Coord
import Map
import theGame

import random

class Room(object):
    def __init__(self,c1=Coord(1,1),c2=Coord(2,2)):
        self.c1=c1
        self.c2=c2
    
    def __repr__(self):
        return f"[<{self.c1.x},{self.c1.y}>, <{self.c2.x},{self.c2.y}>]"
        
    def __contains__(self,item):
        if isinstance(item,Coord):
            if self.c1.x<=item.x<=self.c2.x and self.c1.y<=item.y<=self.c2.y:
                return True
        return False
        
    def center(self):
        ord=((self.c2.x)+(self.c1.x))//2
        abs=(self.c2.y + self.c1.y)//2
        return Coord(ord,abs)
        
    def intersect(self,salle):
        if self.c1 in salle or self.c2 in salle or Coord(self.c1.x,self.c2.y) in salle or Coord(self.c2.x,self.c1.y) in salle:
            return True
        if salle.c1 in self or salle.c2 in self or Coord(salle.c1.x,salle.c2.y) in self or Coord(salle.c2.x,salle.c1.y) in self:
            return True
        return False       
        
    def randCoord(self):
        a=random.randint(self.c1.x,self.c2.x)
        b=random.randint(self.c1.y,self.c2.y)
        return Coord(a,b)
        
    def randEmptyCoord(self,map):
        a = 0
        while a==0:
            c=self.randCoord()
            if c!=self.center() and map.get(c)==map.ground:
                a = 1
            else:
                a = 0
        return c
    
    def decorate(self,map):
        map.put(self.randEmptyCoord(map),theGame.theGame().randEquipment())
        map.put(self.randEmptyCoord(map),theGame.theGame().randMonster())
        
