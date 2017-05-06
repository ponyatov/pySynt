from Object import *
class String(Object):
    def head(self): return '\'%s\' # %X'%(self.val,id(self))    
    def __add__(self,o): return String(self.val + o.str().val)
