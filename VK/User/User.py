from VK.Object import Object
import VK.User

class User(Object):
    _init_collections_ = {
        'friends': lambda: VK.User.Friends(),
        'subscriptions': lambda: VK.User.Subscriptions(),
        'followers': lambda: VK.User.Followers(),
        'groups': lambda: VK.User.Groups()
    }

    def _init_instance_of_(self):
        return VK.User.Users()