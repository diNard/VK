import VK
from VK.Collection import Collection
from VK.Groups import Groups
from VK.Group import Group
from VK.User.Users import Users

class Subscriptions(Collection):
    __counts = {'users': None, 'groups': None}

    def _init_children_():
        return ['users', 'groups']

    def _init_load_(self):
        return [
            'users.getSubscriptions',
            {'uid' : self.parent().id, 'extended': '1'},
            self._callback_
        ]

    def _callback_(self, response):
        self.__response['users'] = Users()
        self.__response['groups'] = Groups()

        if 'users' in response:
            self.__separately(response)
        else:
            self.__together(response)
        return {}

    def __separately(self, response):
        for _id in response['users']['items']:
            self.__response['users'].append(VK.User(_id))
        
        for _id in response['groups']['items']:
            self.__response['groups'].append(Group(_id))

        self.__counts = {
            'users': response['users']['count'],
            'groups': response['groups']['count']
        }

    def __together(self, response):
        for item in response:
            if 'uid' in item:
                self.__response['users'].append(VK.User(item['uid'], item))
            else:
                self.__response['groups'].append(Group(item['gid'], item))