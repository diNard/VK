from VK.Root import Root
from VK.Groups import Groups

class Group(Root):
    def _init_load_(self):
        _self = Groups().append(self).load().get_items()[0]
        self.append(_self.get_items())

    def _init_collections_(self):
        return {}