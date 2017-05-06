from Object import *
from String import *
class Vector(Object):
    def __init__(self): Object.__init__(self,'[]')
    def head(self): return '[] # %X'%id(self)
    def __div__(self,o):
        " split list "
        L = Vector()
        for i in self.nest: L += i ; L += o
        L.pop() ; return L
    def str(self):
        S =''
        for i in self.nest: S += i.str().val
        return String(S)