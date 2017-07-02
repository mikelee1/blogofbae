#-*- coding:utf-8 -*-
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE']='webapp.settings'
path = os.path.dirname(os.path.abspath(__file__)) + '/webapp'
if path not in sys.path:
	sys.path.insert(1,path)
from django.core.wsgi import get_wsgi_application
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(get_wsgi_application())