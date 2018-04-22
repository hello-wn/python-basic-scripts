# -*- coding: utf-8 -*-
import re
import urllib
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return  new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        #/item/%E9%A2%84%E5%A4%84%E7%90%86%E5%99%A8
        new_links = soup.find_all('a', href=re.compile(r"/item/(.*)"))
        for link in new_links:
            new_url = link['href']
#            print(url, new_url)
            new_full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        new_data = {}
        new_data['url'] = url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>PHP</h1>
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = title.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary = soup.find('div', class_='lemma-summary')
        new_data['summary'] = summary.get_text()

        return new_data
