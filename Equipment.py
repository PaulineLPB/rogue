from Element import Element
import theGame


class Equipment(Element):
    def __init__(self,name=None,abbrv="", usage = None):
        Element.__init__(self,name,abbrv)
        if usage==None:
            self.usage=None
        else:
            self.usage=usage
        
    def meet(self,hero):
        hero.take(self)
        theGame.theGame().addMessage("You pick up a "+self._name)
        return True 
    
    def use(self,creature):
        if self.usage!=None:
            theGame.theGame().addMessage("The "+ str(creature._name)+" uses the "+ str(self._name))
            return self.usage(self,creature)
        else:
            theGame.theGame().addMessage("The "+str(self._name)+" is not usable")
            return False
