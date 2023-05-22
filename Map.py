from Coord import Coord
from Hero import Hero
from Room import Room
from Element import Element
from Creature import Creature

import random

class Map(object):
    ground="."
    empty=' '
    dir={'z': Coord(0,-1), 's': Coord(0,1), 'd': Coord(1,0), 'q': Coord(-1,0)}

    
    def __init__(self,size=20,hero=None,roomsToReach=None,rooms=None,nbrooms=7):
        self.size=size
        if hero==None:
            self._hero=Hero()
        else:
            self._hero=hero
        self._mat=[]
        if roomsToReach is None:
            self._roomsToReach=[]
        else:
            self._roomsToReach=roomsToReach
        if rooms is None:
            self._rooms=[]
        else:
            self._rooms=rooms
        for i in range(self.size):
            l=[]
            for j in range(self.size):
                l.append(Map.empty)
            self._mat.append(l)
        self.nbrooms=nbrooms
        self.generateRooms(nbrooms)
        self.reachAllRooms()
        self._mat[self._rooms[0].center().y][self._rooms[0].center().x]=self._hero
        self._elem={self._hero:self._rooms[0].center()}     #self._elem={self._hero : self.posi}
        for room in self._rooms:
            room.decorate(self)


        
    def __repr__(self):
        c=""
        for i in range(self.size):
            for x in range(self.size):
                c=c+str(self._mat[i][x])
            c=c+'\n'
        return c
        
    def __len__(self):
        return self.size
        
    def __contains__(self, item):
        if isinstance(item,Coord):
            if 0<=item.x<len(self) and 0<=item.y<len(self):
                return True
        elif self._elem.get(item) or item==Map.ground:
            return True
        return False 
    
    def get(self,c):
        self.checkCoord(c)
        if c in self:
            return self._mat[c.y][c.x]
    
    def pos(self,e):
        self.checkElement(e)
        if e in self:
            return self._elem[e]
            
    def put(self,c,e):
        self.checkCoord(c)
        self.checkElement(e)
        if self._mat[c.y][c.x]!=Map.ground:
            raise ValueError('Incorrect cell') 
        if e in self._elem:
            raise KeyError('Already placed')
        self._mat[c.y][c.x]=e
        self._elem[e]=c
            
    def rm(self,c):
        self.checkCoord(c)
        del self._elem[self._mat[c.y][c.x]]
        self._mat[c.y][c.x]=Map.ground

                    
    def verif_cord(self,c):
            if  0 <= c.x and c.x < self.size and 0 <= c.y and c.y < self.size:
                return True
            return False

    def move(self,e,way):
        newpos = self.pos(e)
        if self.verif_cord(newpos+way):
            if self.get(newpos+way) == self.ground:
                self.rm(newpos)
                self.put(way+newpos,e)
            elif not self.get(newpos+way) == self.empty:
                el = self.get(newpos+way)
                if el.meet(e):
                    self.rm(newpos+way)
                    
    def moveMonster(self, e, way):
        """Moves the element e in the direction way."""
        orig = self.pos(e)
        dest = orig + way
        if dest in self:
            if self.get(dest) == Map.ground:
                self._mat[orig.y][orig.x] = Map.ground
                self._mat[dest.y][dest.x] = e
                self._elem[e] = dest
            elif self.get(dest) != Map.empty and self.get(dest) != self._hero:
                None
            elif self.get(dest)==self._hero:
                self.get(dest).meet(e)

    
    def addRoom(self,room):             #Ajout d'une room
        self._roomsToReach.append(room)
        for i in range(room.c1.x,room.c2.x+1):
            for o in range(room.c1.y,room.c2.y+1):
                self._mat[o][i]=Map.ground
    
    def findRoom(self,coord):           #retourne la salle, parmi _roomsToReach, qui contient la coordonnée coord. Retourne False si aucune salle ne correspond.
        for room in self._roomsToReach:
            if coord in room:
                return room
        return False

    def intersectNone(self,room):       #retourne True si aucune salle, parmi _roomsToReach, n'a une intersection avec room, False sinon.
        for i in range(len(self._roomsToReach)):
            if self._roomsToReach[i].intersect(room):
                return False
        return True
        
    def dig(self,coord):                #Change une coord en un point et si c'est une room l'enlève de RTC et la met dans rooms
        self._mat[coord.y][coord.x]=Map.ground
        b=self.findRoom(coord)
        if b!=False:
            self._rooms.append(b)
            self._roomsToReach.remove(b)
            
    def corridor(self, start, end):
        startY=start
        startX=start
        self.dig(start)
        if start.y<end.y:
            for case in range(0,end.y-start.y):
                startY.y=startY.y+1
                self.dig(startY)
        else:
            for case in range(0,start.y-end.y):
                startY.y=startY.y-1
                self.dig(startY)
        
        if start.x<end.x:
            for case in range(0,end.x-start.x):
                startX.x=startX.x+1
                self.dig(startX)
        else:
            for case in range(0,start.x-end.x):
                startX.x=startX.x-1
                self.dig(startX)
        
    def reach(self):
        a=random.choice(self._rooms)
        b=random.choice(self._roomsToReach)
        self.corridor(a.center(),b.center())
        
    def reachAllRooms(self):
        self._rooms.append(self._roomsToReach[0])
        self._roomsToReach.remove(self._roomsToReach[0])
        while self._roomsToReach:
            self.reach()
            
    def randRoom(self):
        x1=random.randint(0,len(self)-3)
        y1=random.randint(0,len(self)-3)
        largeur=random.randint(3,8)
        longueur=random.randint(3,8)
        x2=min(x1+largeur,len(self)-1)
        y2=min(y1+longueur,len(self)-1)
        return Room(Coord(x1,y1),Coord(x2,y2))
        
    def  generateRooms(self,n):
        for i in range(n):
            newRoom=self.randRoom()
            if self.intersectNone(newRoom):
                self.addRoom(newRoom)
    
    def checkCoord(self,c):
        if not isinstance(c,Coord):
            raise TypeError('Not a Coord') 
        if c not in self:
            raise IndexError('Out of map coord')
            
    def checkElement(self,c):
        
        if not isinstance(c,Element):
            raise TypeError('Not a Element') 
    
    def moveAllMonsters(self):
        for (key,element) in self._elem.items():
            if isinstance(key,Creature) and isinstance(key,Hero)==False:
                if self._elem[key].distance(self._elem[self._hero])<6:
                    self.moveMonster(key,self._elem[key].direction(self._elem[self._hero]))
                    
                
