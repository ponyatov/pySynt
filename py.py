
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
  		self['exe' ] = self['dir']/String(self.val+'.exe') ; self['exe'].rm()
  		self['log' ] = self['dir']/String(self.val+'.log') ; self['files'] += self['log']
  		self['hpp'] = self['dir']/String('hpp.hpp') ; self['files'] += self['hpp']
  		self['cpp'] = self['dir']/String('cpp.cpp') ; self['files'] += self['cpp']
  		self['mk' ] = self['dir']/String('Makefile') ; self['files'] += self['mk']
		self['bat'] = self['dir']/String('bat.bat') ; self['files'] += self['bat']
  		self['git'] = self['dir']/String('.gitignore') ; self['files'] += self['git']
  	def build_cpp(self):
  		# hpp.hpp
  		self['hpp']/String('#ifndef _H_HPP')/String('#define _H_HPP')
  		self['hpp']/String('#endif // _H_HPP')
  		# cpp.cpp
  		self['cpp']/(String('#include "')+self['hpp']+String('"'))
  		self['cpp']/String('int main(int argc, char *argv[]) { return 0; }')
  		# Makefile
		self['mk']/(String('C = ')+self['cpp'])
		self['mk']/(String('H = ')+self['hpp'])
		self['mk']/(String('')+self['exe'] + String(' : $(C) $(H)'))
		self['mk']/(String('\t$(CXX) $(CXXFLAGS) -o $@ $(C) $(L)'))
	def build(self):
		# Makefile
		self['mk']/(self['log'].str() + String(' : ') + self['exe'])
		self['mk']/(String('\t./')+self['exe']+String(' > $@'))
		# hpp/cpp
		self.build_cpp()
		# bat.bat
		self['bat']/( String('@gvim -p ') + (self['files']/String(' ')).str() )
		# .gitignore
		self['git']/String('*~')/String('*.swp')/self['exe']/self['log']
		return self

print Module('Hello').build()
