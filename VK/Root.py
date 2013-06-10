from VK.Base import Base

class Root(Base):

    def __init__(self, id, data = []):
        super(Root, self).__init__()
        self.id = id
        self.append(data)


    def set(self, data, value = None):
        return self.append(data, value)