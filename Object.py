class Object:
	" core object class "
	def __init__(self, V):
		" create object "
		self.tag = self.__class__.__name__.lower() ; self.val = V
		self.nest = [] ; self.attr = {} ; self.sync = False 
	def __finalize__(self):
		" synchronous finalizer "
		for i in self.attr: self.attr[i].__finalize__()
		for j in self.nest: j.__finalize__()
	# dump object
	def __repr__(self): return self.dump()
	def head(self): return '<%s:%s> #sync:%.1i # %X' % \
		(self.tag, self.val, self.sync, id(self))
	def pad(self,depth,S): return '\n' + '\t'*depth + S  
	dump_infty = []
	def dump(self, depth=0, prefix=''):
		# block infty dumping
		if depth==0: self.dump_infty = [] 
		if self in self.dump_infty: return self.pad(depth,self.head()+' ...')
		self.dump_infty.append(self)
		# header
		S = self.pad(depth,prefix + self.head())
		# attr{}ibutes
		for i in self.attr: S += self.attr[i].dump(depth + 1, '%s = ' % i)
		# nest[]ed
		N = 0
		for j in self.nest: S += j.dump(depth + 1, '%.2i: ' % N) ; N += 1
		# return dump
		return S
	# operators
	def str(self): return self.val
	def __div__(self, o): self.nest.append(o) ; return self
	def __setitem__(self,K,V): self.attr[K] = V
	def __getitem__(self,K):
		if type(K) == int: return self.nest[K]
		else: return self.attr[K]
