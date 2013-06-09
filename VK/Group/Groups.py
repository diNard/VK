from VK.Collection import Collection
from VK.Group import Group

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