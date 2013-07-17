
class App:

	def has_user(self, user):
    	return self.request('users.isAppUser', {'uid': user.id}) == 1