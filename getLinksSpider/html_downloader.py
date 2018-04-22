# -*- coding: utf-8 -*-

from urllib import request

class HtmlDownloader(object):

    def download(self, new_url):
        if new_url is None:
            return None
        
        with request.urlopen(new_url) as f:
            if f.getcode() != 200:
                return None
            return f.read()
