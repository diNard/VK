import urllib
import json
import VK

class Request(object):
	__items = {}
	__params = {}

	__need_load = False
	__loaded = False

	def __load(self):
		if (self.__need_load == True) and (self.__loaded == False):
			settings = self._init_load_()

			method = settings[0] or ''
			params = dict( (settings[1] or {}).items() + self.__params.items() )
			callback = settings[2] or (lambda result: result)

			response = self.__request(method, params)
			self.__items = callback(response)
			self.__loaded = True

	def __request(self, method, params):
		url_params = "&".join( list("%s=%s" % (str(key), str(params[key])) for key in params) )
		response = urllib.urlopen('https://api.vk.com/method/%s?%s' % (method, url_params)).read()
		return json.loads(response)['response']

	# ========== PUBLIC ===============

	def load(self):
		self.__need_load = True
		return self

	def filter(self, data, value):
		if isinstance(data, basestring):
			self.__params[ str(data) ] = value
		elif isinstance(data, dict):
			self.__params = dict(self.__params.items() + data.items())
		return self

	def append(self, data, value = None):
		if isinstance(data, VK.Root.Root):
			self.__items[ str(data.id) ] = data
		elif isinstance(data, list):
			list(self.append(item) for item in data)
		elif isinstance(data, dict):
			self.__items = dict(self.__items.items() + data.items())
		if isinstance(data, basestring) or isinstance(data, (int, long)):
			self.__items[ str(data) ] = value
		return self

	def get_keys(self):
		return self.__items.keys()

	def get_items(self):
		self.__load()
		return self.__items