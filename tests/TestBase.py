from nose.tools import assert_raises
from VK.Base import Base

class TestBase:
    def setUp(self):
        pass

    def teardown(self):
        pass

    def test_filter(self):
        b = Base()

        # append items
        b.filter('ag', 20)
        assert b.get_filters() == {'ag': 20}

        b.filter(40, 40)
        assert b.get_filters() == {'ag': 20, '40': 40}

        b.filter({'test': 'test'})
        assert b.get_filters() == {'ag': 20, '40': 40, 'test': 'test'}

        # rewrite items
        b.filter({'40': 'rewrote'})
        assert b.get_filters() == {'ag': 20, '40': 'rewrote', 'test': 'test'}

        b.filter('ag', 'tet')
        assert b.get_filters() == {'ag': 'tet', '40': 'rewrote', 'test': 'test'}

        # reset
        b.reset()
        assert b.get_filters() == {}

        # append list
        b.filter([{20: 20}, {'re': 're_value', 'new': 'new'}])
        assert b.get_filters() == {'20': 20, 're': 're_value', 'new': 'new'}

        # append without values
        b.reset()
        b.filter(40)
        assert b.get_filters() == {'40': None}

        b.filter({60: None})
        assert b.get_filters() == {'40': None, '60': None}

        b.filter([4, 5])
        assert b.get_filters() == {'40': None, '60': None, '4': None, '5': None}

        # append incorrect values
        base = Base()
        b.reset()
        b.filter('a', base)
        assert b.get_filters() == {'a': None}

        b.filter({'b': base})
        assert b.get_filters() == {'a': None, 'b': None}

        # append incorrect keys
        b.reset()
        b.filter(base, 'test')
        assert b.get_filters() == {}

        b.filter({base, 'test'})
        assert b.get_filters() == {}

        b.filter([base])
        assert b.get_filters() == {}



