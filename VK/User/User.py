from VK.Root import Root
from VK.User.Users import Users
from VK.User.Friends import Friends
from VK.Subscriptions import Subscriptions
from VK.User.Followers import Followers
from VK.User.Groups import Groups as User_groups

class User(Root):

    def _init_load_(self):
        _self = Users().append(self).load().get_items()[0]
        self.append(_self.get_items())

    def _init_collections_(self):
        return {
            'friends': lambda: Friends().parent(self).load(),
            'subscriptions': lambda: Subscriptions().parent(self).load(),
            'followers': lambda: Followers().parent(self).load(),
            'groups': lambda: User_groups().parent(self).load()
        }

# users.isAppUser : no access token : current