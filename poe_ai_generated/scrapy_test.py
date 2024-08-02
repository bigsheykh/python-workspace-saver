import scrapy
from warnings import catch_warnings


d = {'a': 123, u'b': b'c', u'd': u'e', 77: u'e'}
d2 = scrapy.utils.python.stringify_dict(d, keys_only=False)

tuples = [('a', 123), (u'b', 'c'), (u'd', u'e'), (77, u'e')]
d3 = dict(tuples)
d4 = scrapy.utils.python.stringify_dict(tuples, keys_only=False)

d5 = {'a': 123, u'b': 'c', u'd': u'e', 77: u'e'}
d6 = scrapy.utils.python.stringify_dict(d5)

with catch_warnings(record=True) as warnings:
    a_dict_item = scrapy.item.DictItem()
    print(len(warnings))
