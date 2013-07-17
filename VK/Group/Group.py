from VK.Object import Object
import VK.Group

class Group(Object):
	
    def _init_load_(self):
        _self = Groups().append(self).load().get_items()[0]
        self.append(_self.get_items())

    # Check whether user is member of the group
    # groups.isMember: no access
    def is_member(self, user):
    	res = self.request('groups.isMember', {'gid': self.id, 'uid': user.id})
    	if 'member' in res:
    		
    	else:
    		return res == 1