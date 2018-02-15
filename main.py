from gevent import monkey, pywsgi
# Replace standard lib functions with gevent-friendly equivalents
monkey.patch_all()

from bundleservice.service import api

if __name__ == '__main__':
    address = ''
    port = 8080
    server = pywsgi.WSGIServer((address, port), api)
    server.serve_forever()
