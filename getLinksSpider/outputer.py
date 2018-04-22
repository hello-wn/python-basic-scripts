# -*- coding: utf-8 -*-
class Outputer(object):
    def __init__(self):
        self.data_list = []

    def collect_data(self, new_data):
        if new_data is None:
            return None
        self.data_list.append(new_data)

    def output(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write('<table>')
        for data in self.data_list:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
