class Stack:
	def __init__(self):
		self._storage = []
	
	def __len__(self):
		return len(self._storage)

	def push(self,var):
		self._storage.append(var)
		return True

	def pop(self):
		try:
			item = self._storage.pop()
		except IndexError:
			item = None
		return item


