from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):
    timeFlag = None
    flag = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'ul'and attrs[0][1] == 'list-recent-events menu':
                self.flag = 1
        if self.flag == 1 and tag == 'time':
            self.timeFlag = 'Time'

    def handle_endtag(self, tag):
        if tag == 'ul'and self.flag != 0: 
                self.flag = 0

    def handle_data(self, data):
        if self.timeFlag == 'Time':
            print('hahah:')
            print(data)
        self.timeFlag = None

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(data)
