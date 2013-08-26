from VK.base import Object
from VK.base import Collection

class Group(Object):
    def _init_load_(self):
        _self = Groups().append(self).load().get_items()[0]
        self.append(_self.get_items())

    # Check whether user is member of the group
    # groups.isMember: no access
    def is_member(self, user):
    	res = self.request('groups.isMember', {'gid': self.id, 'uid': user.id})
    	if 'member' in res:
    		return true
    	else:
    		return res == 1

class Groups(Collection):
    __fields = [
        'city', 'country', 'place', 'description', 'wiki_page', 'members_count',
        'counters', 'start_date', 'end_date', 'can_post', 'can_see_all_posts',
        'activity', 'status', 'contacts', 'links', 'fixed_post', 'verified'
    ]

    def _init_load_(self):
        return [
            'groups.getById',
            {'gids' : ','.join(self.get_keys()), 'fields' : ','.join(self.__fields)},
            (lambda response: dict((group['gid'], Group(group['gid'], group)) for group in response))
        ]