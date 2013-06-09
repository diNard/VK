from VK.Group import Groups
from VK.Group import Group

class Groups(Groups):
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