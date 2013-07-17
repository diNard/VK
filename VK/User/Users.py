from VK.Collection import Collection
from VK.User import User

class Users(Collection):
    _fields_ = [
        'nickname', 'screen_name', 'sex', 'bdate', 'city', 'country', 'timezone', 
        'photo_50', 'photo_100', 'photo_200_orig', 'has_mobile', 'contacts', 'education', 
        'online', 'counters', 'relation', 'last_seen', 'status', 'can_write_private_message', 
        'can_see_all_posts', 'can_post', 'universities'
    ]

    def _init_load_(self):
        return [
            'users.get',
            {'uids' : ','.join(self.get_keys()), 'fields' : ','.join(self._fields_)},
            (lambda response: dict((user['uid'], User(user['uid'], user)) for user in response))
        ]