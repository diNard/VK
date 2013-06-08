import VK
from VK.Base import VK

class Root(VK):

    def __init__(self, id, data = {}):
        super(Root, self).__init__()
        self.id = id
        self.append(data)


    def set(self, data, value = None):
        return self.append(data, value)