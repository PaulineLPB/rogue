from Element import Element
import theGame


class Creature(Element):
    def __init__(self,name,hp=10,abbrv="",strength=1):
        Element.__init__(self,name,abbrv)
        self._hp=hp 
        self._strength=strength
    
    def description(self):
        return Element.description(self) +"("+str(self._hp)+")"
    
    def meet(self,other):
        self._hp=self._hp-other._strength
        if self._hp<=0:
            theGame.theGame().addMessage("The "+self._name+" hits the "+other.description())
            return True
        theGame.theGame().addMessage("The "+other._name+" hits the "+self.description())
        return False
