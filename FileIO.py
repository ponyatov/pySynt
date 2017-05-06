import os 
from Object import *

class File(Object):
    def __init__(self,D,F):
        Object.__init__(self,F) ; self['dir'] = D ; self.sync = True
    def __finalize__(self):
        if self.sync:
            F = open('%s/%s'%(self['dir'].str(),self.str()),'w')
            for i in self.nest: print >>F,i
            F.close()
            self.sync = False

class Dir(File):
    def __init__(self,D): Object.__init__(self,D)
    def __finalize__(self):
        try: os.mkdir(self.val)
        except WindowsError: pass
        Object.__finalize__(self)
    def __div__(self,o):
        if type(o) == str: V = o
        else: V = o.str()
        if type(o) == str: F = File(self,o)
        else: F = File(self,o.str())
        Object.__div__(self,F)
        return F
