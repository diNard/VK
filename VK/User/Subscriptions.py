from VK.Collection import Collection
from VK.Group import Group
from VK.Group import Groups
from VK.User import User
from VK.User import Users

class Subscriptions(Collection):

    def _init_collections_(self):
        return {
            'groups': lambda: self.__response['groups'],
            'users': lambda: self.__response['users']
        }

    def _init_load_(self):
        return [
            'users.getSubscriptions',
            {'uid' : self.parent().id, 'extended': '1'},
            self._callback_
        ]

    def _callback_(self, response):
        self.__response = {
            'users': Users(),
            'groups': Groups()
        }

        if 'users' in response:
            self.__separately(response)
        else:
            self.__together(response)
        return {}

    def __separately(self, response):
        for _id in response['users']['items']:
            self.__response['users'].append(User(_id))
        
        for _id in response['groups']['items']:
            self.__response['groups'].append(Group(_id))

        self.__counts = {
            'users': response['users']['count'],
            'groups': response['groups']['count']
        }

    def __together(self, response):
        for item in response:
            if 'uid' in item:
                self.__response['users'].append(User(item['uid'], item))
            else:
                self.__response['groups'].append(Group(item['gid'], item))