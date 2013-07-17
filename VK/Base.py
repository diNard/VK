import urllib
import json
from VK.Error import Error

class Base(object):

    def __init__(self):
        self.__items = {}
        self.__params = {}
        self.__loaded = True
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
            self.__ready_collections[name] = self.__collections[name]().parent(self).load()
            return self.__ready_collections[name]

    def __load(self):
        if self.__loaded == False:
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
                if not (response == []):
                    self.__items = callback(response)

    def __request(self, method, params):
        url_params = "&".join( list("%s=%s" % (str(key), str(params[key])) for key in params) )
        print 'https://api.vk.com/method/%s?%s' % (method, url_params)
        response = urllib.urlopen('https://api.vk.com/method/%s?%s' % (method, url_params)).read()
        response = json.loads(response)
        if response.has_key('response'):
            return response['response']
        elif response.has_key('error'):
            raise Error(response['error']['error_code'], response['error']['error_msg'])
        else:
            raise Error(0, 'Unknown')


    def load(self):
        self.__loaded = False
        return self

    def request(self, method, params):
        return self.__request(method, params)

    # Filters
    def filter(self, data, value = None):
        # key, value - just int or string
        if isinstance(data, basestring) or isinstance(data, (int, long)):
            if not isinstance(value, basestring) and not isinstance(value, (int, long)):
                value = None
            self.__params[ str(data).lower() ] = value
        # []
        elif isinstance(data, list):
            for item in data:
                self.filter(item)
        # {}
        elif isinstance(data, dict):
            for k in data:
                self.filter(k, data[k])
        return self

    def reset(self):
        self.__params = {}
        return self

    def get_filters(self):
        return self.__params

    # Items
    def append(self, data, value = None):
        if isinstance(data, Base):
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
