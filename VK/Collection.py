import VK
from VK.Request import Request

class Collection(Request):
	__keys = []
	__items = {}

	def __iter__(self):
		self.__items = self.get_items()
		self.__keys = self.__items.keys()
		return self

	# ------------ Public -------------------
	def next(self):
		if not self.__keys:
			raise StopIteration
		else:
			return self.__items[ self.__keys.pop() ]

	def limit(self, count):
		return self.filter('count', count)