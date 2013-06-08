import VK
from VK.Collection import Collection

class Friends(Collection):
    __fields = [
        'uid', 'first_name', 'last_name', 'sex', 'bdate',
        'city', 'country', 'timezone', 'photo', 'photo_medium',
        'photo_big', 'domain', 'has_mobile', 'education'
    ]

    def _init_load_(self):
        return [
            'friends.get',
            {'uid' : self.get_keys()[0], 'order': 'name', 'fields' : ','.join(self.__fields)},
            (lambda response: dict((user['uid'], VK.User(user['uid'], user)) for user in response))
        ]