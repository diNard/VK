from VK.Collection import Collection
from VK.User import User

class Users(Collection):
    __fields = [
        'nickname', 'screen_name', 'sex', 'bdate', 'city', 'country', 
        'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile',
        'contacts', 'education', 'online', 'universities',
        'counters', 'relation', 'last_seen', 'status', 
        'can_write_private_message', 'can_see_all_posts', 'can_post' 
    ]

    def _init_load_(self):
        return [
            'users.get',
            {'uids' : ','.join(self.get_keys()), 'order': 'name', 'fields' : ','.join(self.__fields)},
            (lambda response: dict((user['uid'], User(user['uid'], user)) for user in response))
        ]

# users.search : no access