#!/usr/bin/python
#: optional path to your local python site-packages folder
import sys
import os

main_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(main_dir, 'lib')
sys.path.insert(0, os.path.join(lib_dir, 'flup-1.0.2'))

## !/usr/bin/python
from flup.server.fcgi import WSGIServer
import app

# ------
class ScriptNameStripper(object):
   def __init__(self, app):
       self.app = app

   def __call__(self, environ, start_response):
       environ['SCRIPT_NAME'] = ''
       return self.app(environ, start_response)

app = ScriptNameStripper(app)

if __name__ == '__main__':
    WSGIServer(app).run()
