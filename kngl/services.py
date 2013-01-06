#!/usr/bin/env python
from collections import namedtuple, defaultdict

counter = defaultdict(int)

Category = namedtuple('Category', 'weight code name')

CODE = Category(1, 'code', 'I code...')
SOCIAL = Category(2, 'social', "I'm social")
PICTURE = Category(3, 'picture', 'Pictural!')

class MetaService(type):
    def __new__(cls, name, bases, attrs):
        is_base_class = attrs.get('__metaclass__') == cls
        if not is_base_class:
            if not isinstance(attrs.get('category'), Category):
                raise TypeError('category not defined on {0}'.format(name))

            counter[attrs['category']] += 1
            attrs['weight'] = counter[attrs['category']]

        attrs.setdefault('name', name.lower())
        attrs.setdefault('icon_name', name.lower())

        return type.__new__(cls, name, bases, attrs)

class Service(object):
    __metaclass__ = MetaService

    icon_char = ''
    link = '#'

    def to_dict(self):
        return {}

class GitHub(Service):
    icon_char = u'\ue002'
    category = CODE
    link = 'https//github.com/KangOl'

class Launchpad(Service):
    icon_char = u'\ue00a'
    category = CODE
    link = 'https://launchpad.net/~kangol'

class Bitbucket(Service):
    icon_char = u'\ue008'
    category = CODE
    link = 'https://bitbucket.org/KangOl'

class Twitter(Service):
    icon_char = u'\ue00d'
    category = SOCIAL
    link = 'https://twitter.com/KangOl'

class LinkedIn(Service):
    icon_char = u'\ue00c'
    category = SOCIAL
    link = 'http://www.linkedin.com/in/simonischristophe'

class Instagram(Service):
    icon_char = u'\ue00f'
    category = PICTURE
    link = 'https://instagr.am/kngl'

class Flickr(Service):
    icon_char = u'\ue011'
    category = PICTURE
    link = 'http://www.flickr.com/photos/kangol/'

_services = {}
for s in Service.__subclasses__():
    _services[s.name] = s()

def get_all_services():
    return _services.values()

def get_service(name):
    return _services.get(name)
