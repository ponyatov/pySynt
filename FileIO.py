import os 
from Object import *
from String import *

class File(Object):
    def fullpath(self): return '%s/%s'%(self['dir'].str().val,self.str().val)
    def __init__(self,D,F):
        Object.__init__(self,F.str().val) ; self['dir'] = D
        self.fh = open(self.fullpath(),'w')
    def __div__(self,o): self += o ; print >>self.fh,o.str().val ; return self
    def str(self): return String(self.val)
    def rm(self): self.fh.close() ; os.remove(self.fullpath())

class Dir(Object):
    def __init__(self,V):
        Object.__init__(self,V)
        try: os.mkdir(self.val)
        except: pass
    def __div__(self,o): F = File(self,o.str()) ; self += F; return F 
