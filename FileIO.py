import os 
from Object import *

class File(Object): pass

class Dir(File):
    def __finalize__(self): os.mkdir(self.val)
