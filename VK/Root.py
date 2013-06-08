import VK
from VK.Base import VK

class Root(VK):
    __collections = {}

    def __init__(self, id, data = {}):
        super(Root, self).__init__()
        self.id = id
        self.append(data)
        self.__collections = self._init_collections_()

    def __getattr__(self, name):
        data = self.get_items()
        if data.has_key(name):
            return data[name]
        elif name in self.__collections:
            return self.__collections[name]()


    def set(self, data, value = None):
        return self.append(data, value)