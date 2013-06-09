from VK.Base import Base

class Collection(Base):
    
    def __init__(self):
        super(Collection, self).__init__()
        self.__keys = []
        self.__items = {}
        self.__parent = None

    def __iter__(self):
        self.__items = self.get_items()
        self.__keys = self.__items.keys()
        return self


    def next(self):
        if not self.__keys:
            raise StopIteration
        else:
            return self.__items[ self.__keys.pop() ]

    def limit(self, count):
        return self.filter('count', count)

    def parent(self, parent = False):
        if isinstance(parent, Base):
            self.__parent = parent
            return self
        else:
            return self.__parent
