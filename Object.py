class Object:
	" core object class "
	def __init__(self, V):
		" create object "
		self.tag = self.__class__.__name__ ; self.val = V
		self.nest = [] ; self.attr = {}
	def __finalize__(self):
		" synchronous finalizer "
		for i in self.attr: self.attr[i].__finalize__()
		for j in self.nest: i.__finalize__()
	def __repr__(self): return self.dump()
	def dump(self, depth=0, pfx=''):
		S = '\n' + '\t' * depth + pfx + self.head()
		for i in self.attr: S += self.attr[i].dump(depth + 1, '%s = ' % i)
		N = 0
		for j in self.nest: S += j.dump(depth + 1, '%.2i: ' % N) ; N += 1
		return S
	def head(self): return '<%s:%s> # %X' % (self.tag, self.val, id(self))
	def __div__(self, o): self.nest.append(o) ; return self
	def __setitem__(self,K,V): self.attr[K] = V
