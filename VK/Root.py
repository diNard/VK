from VK.Request import Request

class Root(Request):
	__collections = {}

	def __init__(self, id, data = {}):
		self.id = id
		self.append(data)
		self.__collections = self._init_collections_()

	def __getattr__(self, name):
		data = self.get_items()
		if data.has_key(name):
			return data[name]
		elif name in self.__collections:
			return self.__collections[name]()

	# ------------ Public -------------------
	def set(self, data, value = None):
		return self.append(data, value)