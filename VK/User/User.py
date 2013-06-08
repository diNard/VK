from VK.Root import Root
from VK.User.Friends import Friends
from VK.Subscriptions import Subscriptions

class User(Root):

    def _init_load_(self):
        _self = VK.Users().append(self).load().get_items()[0]
        self.append(_self.get_items())

    def _init_collections_(self):
        return {
            'friends': lambda: Friends().parent(self).load(),
            'subscriptions': lambda: Subscriptions().parent(self).load()
        }

# users.isAppUser : no access : current