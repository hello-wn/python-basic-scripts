# -*- coding: utf-8 -*-
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

from wsgiref.simple_server import make_server

httpd = make_server('', 8080, application)
print('Serving Http on port 8080...')

httpd.serve_forever()
