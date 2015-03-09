# -*- coding: utf-8 -*-

__author__ = 'cpn'

"""
Примеры взяты вот из этой клевой статьи
http://habrahabr.ru/post/140581/
"""
# std
import json
import urllib
import urllib2


# это класс
class API(object):
    def __init__(self, key, url='http://localhost/'):
        self.header = dict(apikey=key)
        self.url = url

    def call(self, methods, params):
        request = urllib2.Request(
            self.url+methods[0]+'/'+methods[1],
            urllib.urlencode(params),
            self.header
        )

        try:
            response = json.loads(urllib2.urlopen(request).read())
            return response
        except urllib2.HTTPError as error:
            return dict(Error=str(error))


# а это функция
API_KEY = "СЕКРЕТНЫЙ КЛЮЧ"
API_URL = 'https://localhost/%s/%s'

def request(noun, verb, **params):
    headers = {'apikey': API_KEY}
    request = urllib2.Request(API_URL%(noun, verb),
                              urllib.urlencode(params), headers)
    return json.loads(urllib2.urlopen(request).read())
