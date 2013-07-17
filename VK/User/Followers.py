from VK.User import Users
from VK.User import User

class Followers(Users):
    def _init_load_(self):
        return [
            'users.getFollowers',
            {'uid' : self.parent().id,  'fields' : ','.join(self._fields_)},
            (lambda response: dict((user['uid'], User(user['uid'], user)) for user in response['items']))
            # returned also count of followers
        ]