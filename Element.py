class Element(object):
    def __init__(self,name=None,abbrv=""):
        if abbrv=="":
            self._abbrv=name[0]
        else:
            self._abbrv=abbrv
        self._name=name
        
    def __repr__(self):
        return str(self._abbrv)
        
    def description(self):
        return "<"+self._name+">"
        
    def meet(self,hero):
        raise NotImplementedError("Not implemented yet")
        hero.take(self)
        return True 
