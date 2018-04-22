from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

# reference: https://docs.python.org/3.5/library/html.parser.html

class getKeyWordParser(HTMLParser):
    is_get_data = None 
    flag = 0
    res = []
    timeCount = 0
    timeStr = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'ul'and attrs[0][1] == 'list-recent-events menu':
                self.flag = 1
        
        if self.flag == 1:
            if tag == 'a':
                self.is_get_data = 'title'
            elif tag == 'time':
                self.is_get_data = 'time'
            elif tag == 'span' and attrs[0][1] == 'event-location':
                self.is_get_data = 'location'
    
    def handle_endtag(self, tag):
        if self.flag != 0 and tag == 'ul':
            self.flag = 0

    def handle_data(self, data):
        tmp_dict = {}
        if self.flag == 1:
            if self.is_get_data == 'title':
                tmp_dict['title'] = data
                self.is_get_data = None
            elif self.is_get_data == 'time':
                if self.timeCount == 0:
                    self.timeStr =  data.strip() + " - "
                    self.timeCount += 1
                elif self.timeCount == 1:
                    self.timeStr += data.strip()
                    tmp_dict['time'] = self.timeStr
#                    print("timeStr: ", self.timeStr)
                    self.is_get_data = None
                    self.timeStr = ''
                    self.timeCount = 0
            elif self.is_get_data == 'location':
                tmp_dict['location'] = data
                self.is_get_data = None
            if len(tmp_dict) > 0:
                self.res.append(tmp_dict)

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parse = getKeyWordParser()
parse.feed(data)
for item in parse.res:
    for key in item:
        print(key, ": ", item[key])


# output:
# title :  HackWeakEnd Technology Event
# time :  27 April - 29 April
# location :  Bijilo, The Gambia
# title :  PyCamp Baradero 2018 (PyAr Community)
# time :  28 April - 02 May
# location :  Baradero, Buenos Aires Province, Argentina

