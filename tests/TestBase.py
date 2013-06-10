from nose.tools import assert_raises
from VK.Base import Base

class TestBase:
	def setUp(self):
		pass

	def teardown(self):
		pass

	def test_filter(self):
		base = Base()
		base.filter('ag', 20)
		print base.get_keys()
		assert base.get_keys() == {'ag': 20}