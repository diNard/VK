from VK.User import Users
from VK.User import User

class Followers(Users):
    _fields = ['nickname', 'screen_name', 'sex', 'bdate',
    	'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 
    	'has_mobile', 'rate', 'contacts', 'education', 'online']

    def _init_load_(self):
        return [
            'users.getFollowers',
            {'uid' : self.parent().id,  'fields' : ','.join(self._fields)},
            (lambda response: dict((user['uid'], User(user['uid'], user)) for user in response['items']))
        ]