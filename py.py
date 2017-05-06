
from Object import *
from String import *
from Vector import *
from FileIO import *

class Module(Object):
	" program module "
	def __init__(self, V):
		Object.__init__(self, V)
		self['dir'] = Dir(self.val)
		self['files'] = Vector()
		self['hpp'] = self['dir'] / 'hpp.hpp' ; self['files']/self['hpp']
		self['cpp'] = self['dir'] / 'cpp.cpp' ; self['files']/self['cpp']
		self['mk'] = self['dir'] / 'Makefile' ; self['files']/self['mk']
		self['bat'] = self['dir'] / 'bat.bat' ; self['files']/self['bat']
		self['git'] = self['dir'] / '.gitignore' ; self['files']/self['git']
	def build(self):
		self['bat'] / '@gvim -p '
		for i in self['files']: self['bat'] / Str(i)
		print self
		self.__finalize__()

dot = Module('Hello') ; print dot ; dot.build()
