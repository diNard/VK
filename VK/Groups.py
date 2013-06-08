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
            'groups.get',
            {'uid' : self.id, 'extended': '1', 'fields' : ','.join(self.__fields)},
            (lambda response: dict((user['uid'], VK.User(user['uid'], user)) for user in response))
        ]