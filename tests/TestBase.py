from nose.tools import assert_raises
from VK.Base import Base

class TestBase:
    def setUp(self):
        pass

    def teardown(self):
        pass

    # .filter
    # .reset
    # .get_filters
    def test_filter(self):
        b = Base()

        # append items
        b.filter('years', 20)
        assert b.get_filters() == {'years': 20}

        b.filter('TolOWer', 'CASE')
        assert b.get_filters() == {'years': 20, 'tolower': 'CASE'}

        b.filter(40, 40)
        assert b.get_filters() == {'years': 20, 'tolower': 'CASE', '40': 40}

        b.filter({'name': 'viktor'})
        assert b.get_filters() == {'years': 20, 'tolower': 'CASE', '40': 40, 'name': 'viktor'}

        # rewrite items
        b.filter({'40': 'test'})
        assert b.get_filters() == {'years': 20, 'tolower': 'CASE', '40': 'test', 'name': 'viktor'}

        b.filter('years', 'young')
        assert b.get_filters() == {'years': 'young', 'tolower': 'CASE', '40': 'test', 'name': 'viktor'}

        # reset
        b.reset()
        assert b.get_filters() == {}

        # append list
        b.filter([{20: 20}, {'city': 'Kiev', 'state': 'Ukraine'}])
        assert b.get_filters() == {'20': 20, 'city': 'Kiev', 'state': 'Ukraine'}

        # append without values
        b.reset()
        b.filter(40)
        assert b.get_filters() == {'40': None}

        b.filter({60: None})
        assert b.get_filters() == {'40': None, '60': None}

        b.filter(['test', 5])
        assert b.get_filters() == {'40': None, '60': None, 'test': None, '5': None}

        # append incorrect values
        base = Base()
        b.reset()
        b.filter('a', base)
        assert b.get_filters() == {'a': None}

        b.filter({'b': base})
        assert b.get_filters() == {'a': None, 'b': None}

        b.filter('c', [])
        assert b.get_filters() == {'a': None, 'b': None, 'c': None}

        b.filter('d', {'10': 10})
        assert b.get_filters() == {'a': None, 'b': None, 'c': None, 'd': None}

        b.filter('e')
        assert b.get_filters() == {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}

        # append incorrect keys
        b.reset()
        b.filter(base, 'test')
        assert b.get_filters() == {}

        b.filter({base, 'test'})
        assert b.get_filters() == {}

        b.filter([base])
        assert b.get_filters() == {}

        b.filter([])
        assert b.get_filters() == {}

        b.filter({})
        assert b.get_filters() == {}

        # returns:
        assert b.filter('test', 1) == b

    def test_reset(self):
    	b = Base()
    	
    	# returns:
    	assert b.reset() == b


