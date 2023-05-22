from Equipment import Equipment
from Creature import Creature
from Coord import Coord
from Hero import Hero
from Map import Map
from Stairs import Stairs
from handler import heal, teleport
from utils import getch
import theGame

import random, copy

class Game(object):
    equipments = { 0: [ Equipment("potion","$",usage=lambda self, hero: heal(hero)), Equipment("gold","o") ], 1: [ Equipment("potion","!",usage=lambda self, hero: teleport(hero, True)),Equipment("sword"), Equipment("bow") ], 2: [ Equipment("chainmail") ], 3: [ Equipment("portoloin","w",usage=lambda self, hero: teleport(hero, False))] }
    monsters = { 0: [ Creature("Goblin",4), Creature("Bat",2,"W") ], 1: [ Creature("Ork",6,strength=2), Creature("Blob",10) ], 5: [ Creature("Dragon",20,strength=3) ] }
    _actions = { 'z' : lambda hero : theGame.theGame().__dict__['_floor'].move(hero,Coord(0,-1)), 's' : lambda hero : theGame.theGame().__dict__['_floor'].move(hero,Coord(0,1)), 'q' : lambda hero : theGame.theGame().__dict__['_floor'].move(hero,Coord(-1,0)),'d' : lambda hero : theGame.theGame().__dict__['_floor'].move(hero,Coord(1,0)), 'i' : lambda hero : theGame.theGame().addMessage(hero.fullDescription()), 'k' : lambda hero :hero.__setattr__('_hp',0), ' ' : lambda hero : None, 'u' : lambda hero : hero.use(theGame.theGame().select(hero._inventory))}
    
    def __init__(self,hero=None,level=1,floor=None,message=None):
        if hero==None:
            self._hero=Hero()
        else:
            self._hero=hero
        self._level=level
        self._floor=floor
        if message==None:
            self._message=[]
        else:
            self._message=message
        
    def buildFloor(self):
        self._floor=Map(hero=self._hero)
        self._level+=1
        self._floor.put(self._floor._rooms[-1].center(),Stairs())
        
    
    def addMessage(self,msg):
        self._message.append(msg)
    
    def readMessages(self):
        c=""
        for i in range(len(self._message)):
            c+=str(self._message[i])+". "
        self._message.clear()
        return c
        
    def randElement(self,collection):
        X=int(random.expovariate(1 /self._level))
        menagerie=sorted(collection)
        for a in range(len(menagerie)):
            if menagerie[a] <= X and (menagerie[a]==menagerie[-1] or menagerie[a+1]>X):
                elem=random.choice(collection[menagerie[a]])
        elem2=copy.copy(elem)
        return elem2
        
    def randEquipment(self):
        return self.randElement(self.equipments)
        
    def randMonster(self):
        return self.randElement(self.monsters)
        
    def select(self,l):
        liste=[]
        for i in l:
            liste.append(str(l.index(i))+": "+str(i._name))
        print("Choose item> "+str(liste))
        if getch().isdigit()==False:
            return None
        elif int(getch())>l.index(l[-1]):
            return None
        else:
            return l[int(getch())]
        
    def play(self):
        """Main game loop"""
        self.buildFloor()
        print("--- Welcome Hero! ---")
        while self._hero._hp > 0:
            print()
            print(self._floor)
            print(self._hero.description())
            print(self.readMessages())
            c = getch()
            if c in Game._actions:
                Game._actions[c](self._hero)
            self._floor.moveAllMonsters()
        print("--- Game Over ---")
