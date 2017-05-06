
from Object import *
from FileIO import *

class GitIgnore(File):
    def __init__(self): File.__init__(self, '.gitignore')

class Module(Object):
	" program module "
	def __init__(self, V):
		Object.__init__(self, V)
		self['dir'] = Dir(self.val)
	def build(self):
		self.__finalize__()

dot = Module('Hello') ; print dot ; dot.build()
