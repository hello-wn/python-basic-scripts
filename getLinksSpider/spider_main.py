# -*- coding: utf-8 -*-
import url_manager, html_downloader, html_parser, outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = outputer.Outputer()


    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
         try:
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            count = count + 1
            if count == 10:
               break
         except:
            print('craw failed: %s' % (new_url))
        self.outputer.output()


if __name__=='__main__':
    root_url = 'https://baike.baidu.com/item/PHP/9337?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
