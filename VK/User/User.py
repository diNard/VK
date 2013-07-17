from VK.Object import Object
import VK.User

class User(Object):

    def _init_load_(self):
        _self = Users().append(self).load().get_items()[0]
        self.append(_self.get_items())

    def _init_collections_(self):
        return {
            'friends': lambda: VK.User.Friends(),
            'subscriptions': lambda: VK.User.Subscriptions(),
            'followers': lambda: VK.User.Followers(),
            'groups': lambda: VK.User.Groups()
        }

# users.isAppUser : no access token : current