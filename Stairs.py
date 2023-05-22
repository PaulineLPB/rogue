from Element import Element
import theGame

class Stairs(Element):
    def __init__(self,name="Stairs",abbrv="E"):
        Element.__init__(self,name,abbrv)
    
    def meet(self,hero):
        theGame.theGame().buildFloor()
        theGame.theGame().addMessage("The "+ hero._name+" goes down")
        
