from VK.base import Object
from VK.base import Collection

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

class User(Object):
    _init_collections_ = {
        'friends': lambda: Friends(),
        'subscriptions': lambda: Subscriptions(),
        'followers': lambda: Followers(),
        'groups': lambda: Groups()
    }
    _init_instance_of_ = Users

class Followers(Users):
    def _init_load_(self):
        return [
            'users.getFollowers',
            {'uid' : self.parent().id,  'fields' : ','.join(self._fields_)},
            (lambda response: dict((user['uid'], User(user['uid'], user)) for user in response['items']))
            # returned also count of followers
        ]

class Friends(Collection):
    __fields = [
        'uid', 'first_name', 'last_name', 'sex', 'bdate',
        'city', 'country', 'timezone', 'photo', 'photo_medium',
        'photo_big', 'domain', 'has_mobile', 'education'
    ]

    def _init_load_(self):
        return [
            'friends.get',
            {'uid' : self.parent().id, 'order': 'name', 'fields' : ','.join(self.__fields)},
            (lambda response: dict((user['uid'], User(user['uid'], user)) for user in response))
        ]

from VK.group import Groups as VkGroups
from VK.group import Group as VkGroup
class Groups(VkGroups):
    __fields = [
        'city', 'country', 'place', 'description', 'wiki_page', 'members_count',
        'counters', 'start_date', 'end_date', 'can_post', 'can_see_all_posts',
        'activity', 'status', 'contacts', 'links', 'fixed_post', 'verified'
    ]

    def _init_load_(self):
        return [
            'groups.get',
            {'uid' : self.parent().id,  'extended': '1', 'fields' : ','.join(self.__fields)},
            (lambda response: dict((group['gid'], Group(group['gid'], group)) for group in response[1,]))
        ]

    def groups():
    	self.filter('filter', 'groups')

    def publics():
    	self.filter('filter', 'publics')

    def events():
    	self.filter('filter', 'events')

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
            self.__callback
        ]

    def __callback(self, response):
        self.__response = {
            'users': Users(),
            'groups': VkGroups()
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
                self.__response['groups'].append(VkGroup(item['gid'], item))

class User_Sex:
    config = {
        'type': 'dict',
        'items': {
            0: 'unknown',
            1: 'women',
            2:  'man'
        }
    }


class User_City:
    config = {
        'type': 'vk_object',
        'key': 'id',
        'fields': {
            'id': 0,
            # will be loaded
            'name': ''
        },
        # @todo check it
        'method': 'places.getCityById'

class User_Country:
    config = {
        'type': 'vk_object',
        'key': 'id',
        'fields': {
            'id': 0,
            #will be loaded
            'name': ''
        },
        # @todo check it
        'method': 'places.getCountryById'
    }

class User_Photo:
    config = {
        'type': 'object'
        'fields': {
            'photo_50': '', #http://vk.com/images/camera_c.gif
            'photo_100': '', #http://vk.com/images/camera_b.gif
            'photo_200_orig': '', #http://vk.com/images/camera_a.gif - no quadrate
            'photo_200': '', #no require
            'photo_400_orig': '',#no require - no quadrate
            'photo_max': '', #http://vk.com/images/camera_b.gif
            'photo_max_orig': ''# http://vk.com/images/camera_a.gif - no quadrate
        }
    }

class User_Online:
    config = {
        'type': 'object',
        'fields': {
            'online': 0,
            'online_mobile': 0,
            'online_app': 0 #id of app
        }
    }

class User_Mobile:
    config = {
        'type': 'object',
        'fields': {
            'has_mobile': 0,
            'mobile_phone': '',
            'home_phone': ''
        },
        'import_from_field': 'content'
    }

class User_List_Collection:
    config = {
        'type': 'vk_collection',
        'method': 'friends.getLists'
    }

class User_University:
    config = {
        'type': 'object',
        'fields': {
            'id': 0,
            'country': ['User_Country', 0],
            'city': ['User_City', 0],
            'name': '', 
            'faculty': 0,
            'faculty_name': '', 
            'chair': 0, 
            'chair_name': '',
            'graduation': 0 #0000
        }
    }

class User_Shool:
    config = {
        'type': 'object',
        'fields': {
            'id': 0,
            'country': ['User_Country', 0],
            'city': ['User_City', 0],
            'name': '',
            'year_from': 0, #0000 
            'year_to': 0, #0000 
            'year_graduated': 0, #0000 
            'class': 'a',
            'speciality': '',
            'type': 0,
            'type_str': ''
        }
    } 

class User_Relation:
    config: {
        'type': 'dict',
        'items': {
            0: 'Unknown',
            1: 'Single',
            2: 'In a relationship',
            3: 'Engaged',
            4: 'Married',
            5: "It's Complicated",
            6: 'Actively searching',
            7: 'In love'
        }
    }

class User_Counters():
    config = {
        'type': 'object',
        'fields': {
            'albums': False,
            'videos': False,
            'audios': False,
            'photos': False,
            'notes': False,
            'friends' False,
            'groups': False,
            'online_friends': False,
            'mutual_friends': False,
            'user_videos': False,
            'followers': False,
            # only for desktop
            'user_photos': False,
            'subscriptions': False, #just users
            'pages': False
        }
    }

class User:
    config = {
        'id': 0,
        'first_name': '',
        'last_name': '',

        'sex': ['User_Sex', 0],
        'bdate': '00-00-0000', #may be 'DD-MM'
        'city': ['User_City', 0],
        'country': ['User_Country', 0],

        ':photo': {
            'class': 'User_Photo',
            'type': 'group',
            'fields': {
                'photo_50': '',
                'photo_100': '',
                'photo_200_orig': '',
                'photo_200': '',
                'photo_400_orig': '',
                'photo_max': '',
                'photo_max_orig': ''
            }
        },

        ':online': {
            'class': 'User_Online',
            'type': 'group',
            'fields': {
                'online': 0,
                'online_mobile': 0,
                'online_app': 0
            }
        }
    
        'lists': {
            'class': 'User_Lists',
            'type': 'field',
            'filter': (lambda ids: ','.split(ids))
        },
	
        'screen_name': '', #andrew OR id35828305.

        ':mobile': {
            'class': 'User_Mobile',
            'type': 'group',
            'fields': {
                'has_mobile': 0,
                'contacts': {'mobile_phone': '', 'home_phone': ''}
            }
        }    

        'connections': '', #skype, twitter, livejournal, instagram
        'site': '', #users's site
        'education': {
            'class': 'User_University',
            'type': 'field',
            'convert_fields': {
                'university': 'id',
                'university_name': 'name'
            }
        },

        'universities': ['User_University_Collection', []],
        'schools': ['User_Shools_Collection', []],

        'can_post': 0,
        'can_see_all_posts': 0,
        'can_write_private_message': 0,
        'status': '',
        'status_audio': 0,

        'last_seen': {'time': 0},

        'relation': ['User_Relation', 0]

        'counters': ['User_Counters', {}],
        'nickname': ''
    }
