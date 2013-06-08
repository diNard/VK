import urllib
import json
import VK as VK_module

class VK(object):

    def __init__(self):
        self.__items = {}
        self.__params = {}
        self.__need_load = False
        self.__loaded = False
        self.__collections = {}
        self.__ready_collections = {}

        if "_init_collections_" in dir(self):
            self.__collections = self._init_collections_()

    def __getattr__(self, name):
        name = str(name)
        self.__load()

        if self.__items.has_key(name):
            return self.__items[name]
        elif name in self.__ready_collections:
            return self.__ready_collections[name]
        elif name in self.__collections:
            self.__ready_collections[name] = self.__collections[name]()
            return self.__ready_collections[name]

    def __load(self):
        if (self.__need_load == True) and (self.__loaded == False):
            settings = self._init_load_()
            
            # Some models not return list but call their own function for init data
            # Example: VK.User init VK.Users, get a collection with one item and
            # then copy data of that item to its self.
            if isinstance(settings, list):
                self.__loaded = True

                method = settings[0] or ''
                params = dict( (settings[1] or {}).items() + self.__params.items() )
                callback = settings[2] or (lambda result: result)

                response = self.__request(method, params)
                self.__items = callback(response)

    def __request(self, method, params):
        url_params = "&".join( list("%s=%s" % (str(key), str(params[key])) for key in params) )
        print 'https://api.vk.com/method/%s?%s' % (method, url_params)
        response = urllib.urlopen('https://api.vk.com/method/%s?%s' % (method, url_params)).read()
        return json.loads(response)['response']


    def load(self):
        self.__need_load = True
        return self

    def filter(self, data, value):
        if isinstance(data, basestring) or isinstance(data, (int, long)):
            self.__params[ str(data) ] = value
        elif isinstance(data, dict):
            self.__params = dict(self.__params.items() + data.items())
        return self

    def append(self, data, value = None):
        if isinstance(data, VK_module.Root.Root):
            self.__items[ str(data.id) ] = data
        elif isinstance(data, list):
            list(self.append(item) for item in data)
        elif isinstance(data, dict):
            self.__items = dict(self.__items.items() + data.items())
        elif isinstance(data, basestring) or isinstance(data, (int, long)):
            self.__items[ str(data) ] = value
        return self

    def clear(self):
        self.__items = {}
        return self

    def get_keys(self):
        return self.__items.keys()

    def get_items(self):
        self.__load()
        return self.__items
