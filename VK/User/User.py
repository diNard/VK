from VK.Root import Root
from VK.User.Friends import Friends

class User(Root):
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
			{'uids' : self.id, 'fields' : ','.join(self.__fields)},
			(lambda result: result[0])
		]

	def _init_collections_(self):
		return {
			'friends': lambda: Friends().append(self).load()
		}