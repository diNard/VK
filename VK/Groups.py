import VK
from VK.Collection import Collection

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
            (lambda response: dict((group['gid'], VK.Group.Group(group['gid'], group)) for group in response))
        ]