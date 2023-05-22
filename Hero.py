from Creature import Creature
from Equipment import Equipment


class Hero(Creature):
    def __init__(self,name="Hero",hp=10,abbrv="@",strength=2,inventory=None):
        if inventory is None:
            inventory = []
        Creature.__init__(self,name,hp,abbrv,strength)
        self._inventory=inventory
        
        self._inventoryComplete=[]
        for i in self._inventory:
            self._inventoryComplete.append(i._name)
    
    def description(self):
        return Creature.description(self)+str(self._inventory)
    
    def take(self,elem):
        if not isinstance(elem,Equipment):
            raise TypeError('Not a Element') 
        self._inventory.append(elem)
        self._inventoryComplete.append(elem._name)
    
    def fullDescription(self):
        desc1="> name : "+ str(self.__dict__['_name'])+"\n> abbrv : "+str(self.__dict__['_abbrv'])+"\n> hp : "+str(self.__dict__['_hp'])+"\n> strength : "+str(self.__dict__['_strength'])
        desc2=""
        if len(self.__dict__)>6:
            for (key,element) in self.__dict__.items():
                if key!='_name' and key!='_abbrv' and key!='_hp' and key!='_strength' and key!='_inventory' and key!='_inventoryComplete':
                    desc2+="\n> "+str(key)+" : "+str(self.__dict__[key])
        desc3="\n> INVENTORY : "+str(self.__dict__['_inventoryComplete'])
        desc=desc1+desc2+desc3
        return desc
        
    def use(self,item):
        if not isinstance(item,Equipment):
            raise TypeError('Not a element')
        if item not in self._inventory:
            raise ValueError('Not in inventory')
        if item.use(self)==True:
            self._inventory.remove(item)
            self._inventoryComplete.remove(item._name)
