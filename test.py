def show_friends_list(data):
	c = ''
	for user in data:
		c += "<tr><td><img src='%s'></td><td>%s %s #%s" %(user['photo'], user['first_name'], user['last_name'], user['uid'])
	return c

def show_album_list(data):
	c = ''
	for album in data:
		c += "<tr><td><img src='%s'></td>" % album['thumb_src']
		c += "<td>%s (%s)</td><td>%s</td>" %(album['title'], album['size'], album['description'])
		c += "</tr>"
	return c

def show_notes(data):
	c = ''
	for note in data:
		if not isinstance(note, (int, long)):
			c += "<tr><td>" + note['text'] + "</td><td>Comments: " + str(note['comments']['count']) + "</td><td> Likes:" + str(note['likes']['count']) + "</td></tr>"
	return c
# -------------------------------------------------

#import pycurl

import codecs
 
# Get Friends list from Tatia
#data_str = urllib.urlopen('https://api.vk.com/method/friends.get?uid=4413027&count=200&fields=uid,first_name,last_name,photo&order=name').read()

# Get albums list from Vika
#data_str = urllib.urlopen('https://api.vk.com/method/photos.getAlbums?oid=5855694&need_covers=1').read()


# Get notes from wall Tatia
##data_str = urllib.urlopen('https://api.vk.com/method/wall.get?owner_id=4413027&count=10').read()
#data = json.loads(data_str)['response']

a = '<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><table>'
#a += show_friends_list(data)
#a += show_album_list(data)
#a += show_notes(data)
a += '</table></body></html>'


#file = codecs.open("lol.html", "w", "utf-8")
#file.write(a)
#file.close()
"""

photo = photo.likes.load()

for like in photo.likes
	like.load()

likes = VK.Likes()
likes.add(like2)
likes.add(like3)
likes.load()
# If collection has unsaved items then save it.
likes.save()

likes.load()

albums = VK.User(12).albums.load().likes
OR
albums = VK.User(12).albums.likes
# Because if child of collection not exists we will call function load() for this collection

user.wall.add(note)
note.add_to(user.wall)

photo.save()
note.add(photo)
user.wall.add(note)

# support collection
for post in user.posts:
	for photo in post.photos:
		for like in photo.likes:
			for user in like.users:
				users << user

users = user.posts.photos.likes.users

for user in user.posts.photos.filter(limit = 100, page = 2).likes.users:
	pass

for note in user.friends.wall.notes:
	pass
	# get ids of user
	# get walls of users
	# ...

	#user.friends: array of ids
	if (!self.data.wall):
		self.data.wall = VK.Walls()
		self.data.wall.by_user = self.users.id

	# Walls

user.friends.friends.count()
user.friends.friends.allowed_count()

user.friends.friends.load({page: pageId})
"""
import VK
n = VK.User(4908613)
n.set('number', '007').set({'first_name': 'Viktor'})
print ' --- '
print n.first_name

print n.ggfdf

print n.number

tst = n.friends.limit(3).filter('offset', 2).filter('name_case', 'dat').load()
for k in tst:
	print k.first_name

for j in tst:
	print j.last_name
"""
for gr in n.subscriptions.filter('count', 50).groups:
	print gr.name
 
for us in n.subscriptions.users:
	print us.first_name
"""
"""
print ' ---- Followers --- '
for foll in n.followers.load().limit(5):
	print foll.first_name
"""

gr = VK.Group.Group(11375758)
print gr.is_member(n)


"""
user = VK.User(1)
users = VK.Users().add(user).add(VK.User(2)).load()

for user in users:
	print user

"""